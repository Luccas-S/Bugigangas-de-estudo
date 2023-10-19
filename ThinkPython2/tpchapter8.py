"""
===Strings===

Diferentemente de um int, float ou bool, strings são sequências de valores
ordenados. Aqui veremos mais sobre strings, como acessar seus caracteres
e metodos atrelados à strings.

UMA STRING É UMA SEQUÊNCIA

Strings são sequências de caracteres que o desenvolvedor, usuário ou output
de código ordena. Podemos acessar cada caractere separadamente se usarmos o
operador de colchete:

>>> fruit = 'banana'
>>> letter = fruit[1]

A primeira instrução atribui a string 'banana' para a variável 'fruit'. Já a
segunda instrução usa os colchetes numa expressão chamada índice, que aponta
qual caractere queremos, ela então seleciona o caractere número 1 de fruit e
o atribui a 'letter'.

Mas pode ser que você não obtenha o que espera:

>>> letter
'a'

Apesar do resultado estranho, devemos lembrar que o computador compreende as
coisas de maneira diferente a nós, para humanos, a letra número 1 de 'banana'
é b, porém, na visão do computador, o primeiro componente de algo sempre é o
0. O índice é uma referência do começo da string, e a referência da primeira
letra é zero.

Logo temos uma correção:

>>> letter = fruit[0]
>>> letter
'b'

Concluímos então que b seria a 0ª(zerésima) letra de 'banana', a é a 1ª e n é
a 2ª letra.

Podemos usar uma expressão que contenha variáveis e operadores como índice.

>>> i = 1
>>> fruit[i]
'a'
>>> fruit[i+1]
'n'

Vendo essa possibilidade, não é difícil surgir com uma forma de quebrar o fu-
ncionamento do índice, usando um número de ponto flutuante por exemplo. Para
esses casos o Python nos devolve o seguinte erro:

>>> letter = fruit[1.5]
TypeError: string indices must be integers

LEN

'len' é uma função integrada que nos devolve o número de caracteres de uma
string.

>>> fruit = 'banana'
>>> len(fruit)
6

Para obtermos a última letra de uma string, pode parecer tentador fazer algo
assim:

>>> length = len(fruit)
>>> last = fruit[length]
IndexError: string index out of range

Vemos então um erro de índice, o que ocorre aqui é que não temos nenhuma letr-
a em 'banana' que chegue ao índice 6, por mais contraintuitivo que isso pareç-
a, len calcula o número de caracteres começando do 1 e não do 0, como para o
computador 'banana' vai de 0 a 5, nunca obtemos o caractere 6 que o índice
pede, logo ocorre o erro.

Para acharmos de fato o último caractere podemos então subtrair 1 de length.

>>> last = fruit[length-1]
>>> last
'a'

Podemos também usar índices negativos, esses contam de trás pra frente a par-
tir do fim da string. A expressão fruit[-1] apresenta a última letra, a expr-
essão fruit[-2] vai apresentar a penúltima e assim por diante.

TRAVESSIA COM LOOP FOR

Vamos ver muitos cálculos que processam um caractere por vez em uma string,
começando no início indo caractere por caractere, fazendo algo até chegar ao
fim. Esse tipo de processamento se chama travessia e podemos escrever um ex-
emplo usando loop while:

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


"""