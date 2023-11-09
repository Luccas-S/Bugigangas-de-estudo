"""
===Estudo de caso: jogos de palavras===

LEITURA DE LISTAS DE PALAVRAS

A função integrada open recebe o nome do arquivo como um parâmetro e 
retorna um objeto de arquivo que você pode usar para ler o arquivo.

>>> fin = open('words.txt')

fin é um nome comum de objeto de arquivo usado para entrada de dados. O objeto de arquivo 
oferece vários métodos de leitura, inclusive readline, que lê caracteres no arquivo até 
chegar a um comando de nova linha, devolvendo o resultado como uma string:

>>> fin.readline()
'aa\r\n'

A primeira palavra nesta lista específica é “aa”, uma espécie de lava. A sequência '\r\n' 
representa dois caracteres que representam espaços em branco (whitespace), um retorno de 
carro e uma nova linha, que separa esta palavra da seguinte.

O objeto de arquivo grava a posição em que está no arquivo, então se você chamar readline 
mais uma vez, receberá a seguinte palavra:

>>> fin.readline()
'aah\r\n'

A palavra seguinte é “aah”, uma palavra perfeitamente legítima, então pare de olhar para mim 
desse jeito. Ou, se é o whitespace que está incomodando você, podemos nos livrar dele com o 
método de string strip:

>>> line = fin.readline()
>>> word = line.strip()
>>> word
'aahed'

Você também pode usar um objeto de arquivo como parte de um loop for. Este programa lê 
words.txt e imprime cada palavra, uma por linha:

fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)

EXERCÍCIOS

Exercício 9.1

fin = open('words.txt')

for line in fin:
    word = line.strip()
    if len(word) > 19
        print(word)

Exercício 9.2


"""