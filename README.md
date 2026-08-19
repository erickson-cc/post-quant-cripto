# post-quant-cripto
Repositório destinado ao grupo de estudos em Criptografia Pós-Quântica

# Criptologia
A criptologia se separa em 2 seções: Cripotgrafia e Criptoanálise

## Criptografia
Processo de criptografar informação.
## Criptoanálise
Processo de descriptografar informação.

# Criptografia Simétrica
Duas partes (A e B) querem se comunicar através de um canal aberto (inseguro). A criptografa a mensagem antes de entrar no canal e B deve descriptografar a mensagem após sair do canal. Portanto, temos duas funções, a de criptografar e a de descriptografar. Enquanto a mensagem criptografada passa por um canal inseguro, a chave para rodar as funções é passada por um canal seguro.
# Criptografia Assimétrica (PKc)
Usa duas Chaves, uma pública e outra privada.


# Criptografia baseada em HASH
Os algoritmos criptográficos baseados em HASH são unidirecionais, para descriptografar um resumo criptográfico é necessário uma chave. 

Um esquema de assinaturas consiste em três algoritmos:
= 
# Geração da chave
Produz o par de chaves pública/privada.

# Geração da assinatura
A mensagem do remetente é assinada usando a chave privada.

# Verificação da assinatura
O remetente usa a chave pública para verificar a integridade da mensagem assinada.

Como são unidirecionais, só podem ser quebrados através de brute-force. Um computador quântico consegue acelerar esse processo, portanto, foram desenvolvidos algoritmos de criptografia baseados em HASH que são resistentes ao cenário pós-quântico. Para isso, usam chaves públicas e assinaturas exageradamente longas.

## Algoritmo de SHOR
É usado pelos computadores quânticos para quebrar mensagens criptografadas por algoritmos convencionais. As criptografias pós-quânticas usam reticulados, hashs ou um sistema híbrido de equações para que o algoritmo de shor seja inútil para computadores quânticos. Obviamente quebrar com força-bruta usando um computador quântico seria mais rápido que usando paralelismo nos melhores computadores possíveis. 

O algoritmo de Grover (estudar sobre ele) só consegue reduzir a segurança da chave pela metade, um Hash SHA-256 atacado por um computador quântico oferece a mesma segurança que um hash de 128 bits. Resumindo, o algoritmo de Shor é um atalho que permite que um computador consiga consiga resolver a matemática da criptografia rapidamente, uma criptografia pós-quântica impede esse atalho e força o computador quântico a quebrar o código usando força-bruta (apenas usando chaves maiores?).

## Assinatura de Lamport
- Assinatura de uso único

## WOTS
- Assinatura de uso único
- Cadeias de hash

## Merkle Trees
- Estrutura de árvore
- Cada folha passa por uma função de hash

## XMSS (NIST SP 800-208)
