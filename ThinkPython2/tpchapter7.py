"""
===Iteração===

"Este capítulo é sobre a iteração, a capacidade de executar um bloco de 
instruções repetidamente. Vimos um tipo de iteração, usando a recursividade, 
em “Recursividade”, na página 81. Vimos outro tipo, usando um loop for, em 
“Repetição simples”, na página 65. Neste capítulo veremos ainda outro tipo, 
usando a instrução while. Porém, primeiro quero falar um pouco mais sobre a 
atribuição de variáveis."

REATRIBUIÇÃO

Existe a chance de você já ter chegado ao raciocínio de que podemos fazer
mais de uma atribuição na mesma variável, substituindo o valor antigo por
um novo valor.

>>> x = 5
>>> x
5
>>> x = 7
>>> x
7

Da primeira vez que exibimos x, seu valor é 5; na segunda vez, seu valor
é 7.

Neste ponto quero tratar de uma fonte comum de confusão. Como o Python usa 
o sinal de igual (=) para atribuição, é tentador interpretar uma afirmação 
como a = b como uma proposição matemática de igualdade; isto é, a declaração 
de que a e b são iguais. Mas esta é uma interpretação equivocada.

Em primeiro lugar, a igualdade é uma relação simétrica e a atribuição não é.
Por exemplo, na matemática, se a=7 então 7=a. Mas no Python, a instrução 
a = 7 é legal e 7 = a não é.

Além disso, na matemática, uma proposição de igualdade é verdadeira ou 
falsa para sempre. Se a=b agora, então a sempre será igual a b. No Python, 
uma instrução de atribuição pode tornar duas variáveis iguais, mas elas não 
precisam se manter assim:

>>> a = 5
>>> b = a    # a e b agora são iguais
>>> a = 3    # a e b não são mais iguais
>>> b
5

Como podemos ver, na terceira linha modificamos o valor de a para 3, mas o
valor de b não muda junto, logo elas já não são iguais.

Apesar de ser útil por muitas vezes, devemos usar a reatribuição com prudência.
Se os valores das variáveis mudam com muita frequência, o processo de
leitura e depuração se tornará mais trabalhoso e mais difícil.

ATUALIZAÇÃO DE VARIÁVEIS

Um dos tipos mais comuns de reatribuição é a atualização, onde o novo valor
da variável depende do antigo.

>>> x = x + 1

Esse código acima diz algo como "pegue o valor de x e adicione 1 a ele, 
então atualize x com o novo valor".

Caso tente atualizar uma variável não existente, o próprio Python devolverá
um erro no console, já que o mesmo avalia o lado direito antes da atribuição
de x:

>>> x = x + 1
NameError: name 'x' is not defined

Antes de poder atualizar qualquer variável, é necessário a declarar/iniciali-
zar, isto é feito com uma atribuição simples:

>>> x = 0
>>> x = x + 1

Neste caso de atualização, adicionamos 1 ao valor original de X, essa
atualização chama-se incremento, enquanto que subtrair 1 chama-se decremento.

INSTRUÇÃO WHILE

Computadores são excelentes em realizar tarefas repetitivas sem erros,
podemos automatizar essas tarefas com facilidade usando a repetição, a
repetição também é chamada de iteração. Até o momento desenvolvemos duas
funções, "countdown" e "print_n", ambas usam repetição por meio de recursiv-
idade. Repetições são bem comuns quando estamos programando, logo Python
oferece recursos de linguagem para facilitar o uso de repetições; um deles
é a instrução "for" que vimos préviamente, a que veremos aqui é a "while".

Aqui está uma versão de countdown que usa while como método de repetição:

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

Neste caso, a sintaxe é tão fácil de entender que quase podemos a ler como
sua tradução do inglês, algo como "enquanto n for maior que 0, mostre o valor
de n e entrão decremente dele. Quando chegar a 0, mostre a palavra "Blastoff!""

Mais formalmente, aqui está o fluxo de execução para uma instrução while:

1. Determine se a condição é verdadeira ou falsa.

2. Se for falsa, saia da instrução while e continue a execução da próxima
instrução.

3. Se a condição for verdadeira, execute o corpo e então volte ao passo 1.

Esse tipo de fluxo de repetição chama-se loop, já que o terceiro passo faz
um loop de volta ao topo.

Logo de cara podemos ver que fácilmente podemos quebrar essa repetição se
escrevermos o corpo do while de forma a nenhuma variável mudar, logo, nenhuma
condição é atingida e o loop continuará pra sempre; o corpo deve mudar o valor
de uma ou mais variáveis para evitarmos que se repita infinitamente.

Quando olhamos para countdown, podemos ver a prova de que o loop termina: se
n for zero ou negativo, o loop nunca é executado, caso contrário n ficará
cada vez menor até chegar a 0. Em alguns casos, não é tão fácil perceber isso.

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:        # n é par
            n = n / 2
        else:                 # n é ímpar
            n = n * 3 + 1

A condição deste loop é "n != 1", enquanto n for diferente de 1 o loop cont-
inuará até a condição se tornar falsa.

Cada vez que passa pelo programa, será verificado se n é par ou impar, sendo
par dividiremos n por 2, se for ímpar, substituiremos n por n * 3 + 1.
Por exemplo, se o argumento passado a sequence for 3, os valores resultantes
de n são 3, 10, 5, 16, 8, 4, 2, 1.

Estamos trabalhando aqui com uma conjectura matemática, como n por vezes
aumenta e outras diminui, não temos prova óbvia que n chegará eventualmente
a 1, logo não conseguimos sempre provar que o loop terminará. Para alguns 
valores de n, podemos provar o término. Por exemplo, se o valor inicial for 
uma potência de dois, n será par cada vez que passar pelo loop até que chegue
 a 1. O exemplo anterior termina com uma sequência assim, que inicia com 16.

A questão difícil é se podemos provar que este programa termina para todos 
os valores positivos de n. Por enquanto, ninguém foi capaz de comprovar ou 
refutar isso!

BREAK

O recurso break pode ser muito útil, por vezes não se sabe que está na hora
de terminar um loop até que já esteja na metade do corpo, justamente para isso
o break serve, quebrando o fluxo da repetição e saindo da mesma.

Suponha que você quer receber uma entrada do usuário até que este digite done.
Você pode escrever:

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

No caso a condição do loop que criamos é True, ou seja, sempre será verdadeira
até que chegue à instrução de interrupção, no caso o break.

Cada vez que passa pelo loop, o programa apresenta ao usuário um colchete
angular. Se o usuário digitar done, a instrução break sai do loop. Senão, o
programa ecoa o que quer que o usuário digite e volta ao topo do loop. Aqui
está uma amostra de execução do código acima:

> not done
not done
> done
Done!

Essa é uma das formas mais comuns de escrever um loop while, já que podemos
verificar a condição em qualquer lugar do loop e podemos exprimir a condição
de parada afirmativamente ao invés de negativamente.

RAIZES QUADRADAS



"""