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

Nessa função vemos algo que é o oposto completo do operador '[]', ao contrá-
rio do mesmo, 'find' toma um caractere e encontra o índice onde o caractere
aparece; Caso o caractere esperado não for encontrado, a função retorna -1.

Aqui também vemos o primeiro exemplo de uma instrução return dentro de um
loop, se a condição dada for verdadeira, a função sai do loop e retorna na
hora. Se o caractere não aparece, o programa sai do loop e devolve -1.

O modelo de cálculo usado aqui chama-se busca, atravessamos uma sequência e
retornamos quando encontramos o que estamos procurando.

LOOP E CONTAGEM

No exemplo a seguir o programa conta o número de vezes que um caractere
aparece numa string:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

Este programa demonstra outro padrão de computação chamado contador. 
A variável count é inicializada com 0 e então incrementada cada vez que um 
a é encontrado. Ao sair do loop, count contém o resultado – o número total 
de letras 'a'.

MÉTODOS DE STRINGS

As strings oferecem métodos que executam várias operações úteis. Um método 
é semelhante a uma função – toma argumentos e devolve um valor –, mas a 
sintaxe é diferente. Por exemplo, o método upper recebe uma string e 
devolve uma nova string com todas as letras maiúsculas.

Em vez da sintaxe de função upper(word), ela usa a sintaxe de método 
word.upper():

>>> word = 'banana'
>>> new_word = word.upper()
>>> new_word
'BANANA'

Esta forma de notação de ponto especifica o nome do método, upper e o nome 
da string, word, à qual o método será aplicado. Os parênteses vazios indicam 
que este método não toma nenhum argumento.

Uma chamada de método denomina-se invocação; neste caso, diríamos que 
estamos invocando upper em word.

E, na verdade, há um método de string denominado find, que é notavelmente 
semelhante à função que escrevemos:

>>> word = 'banana'
>>> index = word.find('a')
>>> index
1

Neste exemplo, invocamos find em word e passamos a letra que estamos 
procurando como um parâmetro. Na verdade, o método find é mais geral que a 
nossa função; ele pode encontrar substrings, não apenas caracteres:

>>> word.find('na')
2

Por padrão, find inicia no começo da string, mas pode receber um segundo 
argumento, o índice onde deve começar:

>>> word.find('na', 3)
4

Este é um exemplo de um argumento opcional. find também pode receber um 
terceiro argumento, o índice para onde deve parar:

>>> name = 'bob'
>>> name.find('b', 1, 2)

-1
Esta busca falha porque 'b' não aparece no intervalo do índice de 1 a 2, 
não incluindo 2. Fazer buscas até (mas não incluindo) o segundo índice 
torna find similar ao operador de fatiamento.

OPERADOR IN

A palavra in é um operador booleano que recebe duas strings e retorna True 
se a primeira aparecer como uma substring da segunda:

>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False

Por exemplo, a seguinte função imprime todas as letras de word1 que também 
aparecem em word2:

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

Com nomes de variáveis bem escolhidos, o Python às vezes pode ser lido como 
um texto em inglês. Você pode ler este loop, “para (cada) letra em 
(a primeira) palavra, se (a) letra (aparecer) em (a segunda) palavra, exiba 
(a) letra”.

Veja o que é apresentado ao se comparar maçãs e laranjas:

>>> in_both('apples', 'oranges')
a
e
s

COMPARAÇÃO DE STRINGS

Os operadores relacionais funcionam em strings. Para ver se duas strings 
são iguais:

if word == 'banana':
    print('All right, bananas.')

Outras operações relacionais são úteis para colocar palavras em ordem 
alfabética:

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')

O Python não lida com letras maiúsculas e minúsculas do mesmo jeito que as 
pessoas. Todas as letras maiúsculas vêm antes de todas as letras minúsculas,
portanto:

Your word, Pineapple, comes before banana.
Uma forma comum de lidar com este problema é converter strings em um 
formato padrão, como letras minúsculas, antes de executar a comparação. 
Lembre-se disso caso tenha que se defender de um homem armado com um abacaxi.

DEPURAÇÃO

Ao usar índices para atravessar os valores em uma sequência, é complicado 
acertar o começo e o fim da travessia. Aqui está uma função que supostamente
compara duas palavras e retorna True se uma das palavras for o reverso da 
outra, mas contém dois erros:

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)
    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True

A primeira instrução if verifica se as palavras têm o mesmo comprimento. Se 
não for o caso, podemos retornar False imediatamente. Do contrário, para o 
resto da função, podemos supor que as palavras tenham o mesmo comprimento.

i e j são índices: i atravessa word1 para a frente, enquanto j atravessa 
word2 para trás. Se encontrarmos duas letras que não combinam, podemos 
retornar False imediatamente. Se terminarmos o loop inteiro e todas as 
letras corresponderem, retornamos True.

Se testarmos esta função com as palavras “pots” e “stop”, esperamos o valor 
de retorno True, mas recebemos um IndexError:

>>> is_reverse('pots', 'stop')
...
  File "reverse.py", line 15, in is_reverse
    if word1[i] != word2[j]:
IndexError: string index out of range

Para depurar este tipo de erro, minha primeira ação é exibir os valores dos índices imediatamente antes da linha onde o erro aparece.

while j > 0:
    print(i, j)        # exibir aqui
    if word1[i] != word2[j]:
        return False
    i = i+1
    j = j-1
Agora quando executo o programa novamente, recebo mais informação:

>>> is_reverse('pots', 'stop')
0 4
...
IndexError: string index out of range

Na primeira vez que o programa passar pelo loop, o valor de j é 4, que está 
fora do intervalo da string ‘pots’. O índice do último caractere é 3, então 
o valor inicial de j deve ser len(word2)-1.

Se corrigir esse erro e executar o programa novamente, recebo:

>>> is_reverse('pots', 'stop')
0 3
1 2
2 1
True

Desta vez, recebemos a resposta certa, mas parece que o loop só foi 
executado três vezes, o que é suspeito. Para ter uma ideia melhor do que 
está acontecendo, é útil desenhar um diagrama de estado.

EXERCÍCIOS

Exercício 8.2

fruit = 'banana'
letter = fruit.count('a')
print(letter)


"""