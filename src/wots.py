import math
import secrets ## não é recomendado usar random
import hashlib

"""     ########################
        Geração da chave privada
"""     ########################
def SKlen(hashLen=256, w=8):
    # L = blocos que assinam a mensagem (l1) e blocos que assinam o checksum (l2)
    # l1 = tamanho do hash/w -> 256/8 = 32
    # l2 = valor máximo blocos da mensagem (2^8-1 = 255) -> 255*32 = 8160
    #           2^8 < 8160 < (2^8)^2, logo l2 = 2bytes
    # L = 32+2 = 34 (tamanho da chave privada)
    print("Calculando número de framentos da chave privada...")
    l1 = math.ceil(hashLen/w) # Ceiling of x, the smallest integer greater than or equal to x
    maxBlock = (2**w)-1
    maxSum = maxBlock * l1
    l2 = math.floor(math.log2(maxSum)/w) + 1 # Floor of x, the largest integer less than or equal to x
            # log_2{8160} ~= 12.99, floor(12/8) = 1, 1+1=2
    L = l1+l2
    return L, l1, l2

def SKgen(L, l1=32):
    secret_key = []
    for i in range(L):
        frag = secrets.token_bytes(l1)
        secret_key.append(frag)
    return secret_key

def printSK(sk):
    print("Chave Privada:")
    i=1
    for f in sk:
        print(f"Fragmento {i:2}: {f.hex()}")
        i +=1
    return

def PKgen(sk, w):
    public_key = []
    W=(2**w)-1
    for f in sk:
        f_pk=hashChain(f,W)
        public_key.append(f_pk)
    return public_key

def printPK(sk):
    print("Chave Pública:")
    i=1
    for f in pk:
        print(f"Fragmento {i:2}: {f.hex()}")
        i +=1
    return

"""     #####################
        Geração da Assinatura
"""     #####################

def hashChain(data, iterations):
    f = data
    for i in range(iterations):
        f = hashlib.sha256(f).digest()
    return f

def sign(msg,sk,w=8,ls=2):
    # Hash da mensagem, converte Str para Bytes e faz o hash de 32Bytes
    print("Gerando assinatura da mensagem:"+msg)
    if isinstance(msg, str):
        msg = msg.encode('utf-8')#Strings must be encoded before hashing
    msg_hash = hashlib.sha256(msg).digest()

    # Checksum
    W = (2**w)-1
    checksum_int = 0
    for valor_byte_mensagem in msg_hash:
        checksum_int += (W - valor_byte_mensagem)
    
    checksum_bytes = checksum_int.to_bytes(l2) #transformar checksum_int em l2 bytes
    blocos = list(msg_hash) + list(checksum_bytes) # concatenar l1 + l2 bytes

    assinatura = []
    for i in range(len(blocos)):
        iterations = W - blocos[i]
        #print(f"Blocos[{i}]: {blocos[i]}")
        frag_assinado = hashChain(sk[i], iterations)
        assinatura.append(frag_assinado)

    return assinatura, blocos



"""     ########################
                MAIN()
"""     ########################
w = 8 # Parâmetro de Winternitz
hashLen = 256 # usando SHA256
print("\n"+" "*25+"GERAÇÃO DE CHAVES")
L, l1, l2 = SKlen(hashLen,w)
print(f"L total: {L} fragmentos (Mensagem: {l1} + Checksum: {l2})")

sk = SKgen(L,l1)
print("")
printSK(sk)
print("")

print(f"Tamanho da chave privada gerada: {len(sk)} fragmentos.")
print(f"Tamanho de cada fragmento: {len(sk[0])} bytes.")

pk = PKgen(sk,w)
print("")
printPK(sk)
print("")

print("\n"+" "*25+"GERAÇÃO DE ASSINATURA")
mensagem = "Hello World"
assinatura, blocos_geradores = sign(mensagem, sk, w, l2)

print("Hash da Mensagem + Checksum: ")
print(blocos_geradores)
print(f"\nTamanho da assinatura gerada: {len(assinatura)} fragmentos.")

print("\nAssinatura:")
W = (2**w) - 1
for i, frag in enumerate(assinatura):
    iteracoes_aplicadas = W - blocos_geradores[i]
    print(f"Fragmento {i+1:2}: {frag.hex()} | {iteracoes_aplicadas:3}x")
