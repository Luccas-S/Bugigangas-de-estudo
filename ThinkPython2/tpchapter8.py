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

No caso desse loop temos a variável index que usaremos não só como o índice
que indicará qual letra mostraremos mas também como a condição do loop. A
condição é index<len(fruit), logo, quando index chegar ao final dos carac-
teres de fruit, o loop será interrompido e o último caractere mostrado será
o que tem índice len(fruit)-1.

Outra forma que podemos fazer a mesma coisa é a seguinte:

for letter in fruit:
    print(letter)

Neste caso sempre que o programa executar o loop o caractere seguinte na
string é atribuído à variável letter; O loop continuará até que não sobrem
caracteres.

No próximo exemplo temos o uso de concatenção e loop para fazer uma série
abecedária. No caso usaremos os nomes Jack, Kack, Lack, Mack, Nack, Ouack,
Pack e Quack. O loop produzirá os nomes em ordem:

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)
A saída é:
Jack
Kack
Lack
Mack
Nack
Oack
Pack
Qack

Nesse caso é visivel que não ficou exatamente como deveria ser ja que "Ouack"
e "Quack" foram mal soletrados.

FATIAMENTO DE STRINGS

Segmentos de string são chamados de fatia, podemos selecionar elas da mesma
forma que selecionamos caracteres:

>>> s = 'Monty Python'
>>> s[0:5]
'Monty'
>>> s[6:12]
'Python'

O operador [n:m] retorna a parte da string do “enésimo” caractere ao 
“emésimo” caractere, incluindo o primeiro, mas excluindo o último. 
Este comportamento é contraintuitivo, porém pode ajudar a imaginar os 
índices que indicam a parte entre os caracteres.

Se você omitir qualquer um dos elementos do operador, o mesmo vai proceder de
acordo com qual elemento foi omitido; caso o primeiro seja omitido, a fatia
começará do começo da string, se o segundo for omitido, a fatia procederá
até o fim da string.

>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'

Caso o primeiro elemento(índice) seja maior ou igual ao segundo, teremos uma
string vazia, representada por duas aspas:

>>> fruit = 'banana'
>>> fruit[3:3]
''

Uma string vazia não contém nenhum caractere e tem comprimento 0, fora isso
é igual a qualquer outra string.

STRINGS SÃO IMUTÁVEIS

Vendo a forma como usamos o operador "[]" até agora, se torna interessante a
ideia de usa-lo para atribuir um caractere diferente em uma string que já
possuí atribuição prévia.

>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
TypeError: 'str' object does not support item assignment

Vemos um erro que diz que o objeto(nesse caso a string) não dá suporte a
adição de novos itens(no caso a letra 'J'). Até agora, valores e objetos
não tem inata diferença, además, refinaremos o conceito em breve.

O motivo da tentativa retornar erro é que strings são imutáveis, não podemos
mudar uma string que ja foi declarada, o máximo que poderiamos fazer aqui
seria criar uma variação da primeira string em outra variável.

>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> new_greeting
'Jello, world!'

Apesar de não termos afetado a string original, agora temos uma versão dife-
rente que atende o que queriamos fazer, colocando uma letra nova numa fatia
de 'greeting'.

BUSCANDO

O que faz a seguinte função?

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return-1
"""