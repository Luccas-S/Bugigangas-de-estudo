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

Percebemos que de maneira geral, usamos loops com condições numéricas para
obter resultados também numéricos. Começamos com respostas aproximadas e 
melhoramos essas respostar com cada iteração.

Usaremos de exempo o cálculo de raízes quadradas usando o método de Newton.
Suponha que você queira saber a raiz quadrada de a. Se começar com quase
qualquer estimativa, x, é possível calcular uma estimativa melhor utilizando
uma fórmula para tal(y =(x + a/x)/2)

Por exemplo, se a for 4 e x for 3:
>>> a = 4
>>> x = 3
>>> y = (x + a/x) / 2
>>> y
2.16666666667

O resultado se torna mais e mais preciso com cada iteração do cálculo, usan-
do a estimativa nova cada vez que calcular:

>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.00641025641

Após algumas iterações, a estimativa se torna próxima a exatidão:

>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.00001024003


>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.00000000003

No geral não teremos uma dica de quantas iterações serão necessárias, mas
sabemos quando chegamos lá, afinal ao chegar na exatidão, o resultado para
de mudar.

>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.0

>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.0

Quando y == x podemos parar as iterações, veja aqui um loop que começa com
estimativa inicial x e a melhora até que deixe de mudar, exibindo no fim
o número de iterações feitas para chegar à exatidão:

count = 0
while True:
    count + 1
    print(x)
    y = (x + a/x) / 2
    if y == x:
        print('Number of iterations: '+count)
        break
    x = y

Na maior parte dos casos esse loop funcionará bem, mas quando se trata de 
números float teremos problemas. É difícil ter exatidão entre dois números
de ponto flutuante, maioria dos números racionais como 1/3 e irracionais como
a raiz de 2, não podem ser representados exatamente com um float.

Nesses casos, ao invés de verificar se x e y são exatamente iguais, é mais
seguro usar a função integrada abs, para calcular o valor absoluto ou magnitude
da diferença entre eles:

if abs(y-x) < epsilon:
    break
    
Onde epsilon tem um valor como 0.0000001, que determina a proximidade desejada
entre x e y.

ALGORITMOS

O método de Newton é um exemplo de um algoritmo: um processo mecânico para 
resolver uma categoria de problemas (neste caso, calcular raízes quadradas).

Para entender o que é um algoritmo, pode ser útil começar com algo que não 
é um algoritmo. Quando aprendeu a multiplicar números de um dígito, você 
provavelmente memorizou a tabuada. Ou seja, você memorizou 100 soluções 
específicas. Este tipo de conhecimento não é algorítmico.

No entanto, se você foi “preguiçoso”, poderia ter aprendido alguns truques. 
Por exemplo, para encontrar o produto de n e 9, pode escrever n-1 como o 
primeiro dígito e 10-n como o segundo dígito. Este truque é uma solução 
geral para multiplicar qualquer número de dígito único por 9. Isto é um 
algoritmo!

De forma semelhante, as técnicas que aprendeu, como o transporte na adição, 
o empréstimo na subtração e a divisão longa são todos algoritmos. Uma das 
características de algoritmos é que eles não exigem inteligência para serem 
executados. São processos mecânicos, nos quais cada passo segue a partir do 
último, de acordo com um conjunto de regras simples.

A execução de algoritmos é maçante, mas projetá-los é interessante, 
intelectualmente desafiador e uma parte central da Ciência da Computação.

Algumas coisas que as pessoas fazem naturalmente, sem dificuldade ou 
pensamento consciente, são as mais difíceis para exprimir algoritmicamente. 
A compreensão de linguagem natural é um bom exemplo. Todos nós o fazemos, 
mas por enquanto ninguém foi capaz de explicar como o fazemos, pelo menos 
não na forma de um algoritmo.

DEPURAÇÃO

Ao começar a escrever programas maiores, pode ser que você passe mais tempo 
depurando. Mais código significa mais possibilidades fazer erros e mais 
lugares para esconder defeitos.

Uma forma de cortar o tempo de depuração é “depurar por bisseção”. Por 
exemplo, se há 100 linhas no seu programa e você as verifica uma a uma, 
seriam 100 passos a tomar.

Em vez disso, tente quebrar o problema pela metade. Olhe para o meio do 
programa, ou perto disso, para um valor intermediário que possa verificar. 
Acrescente uma instrução print (ou outra coisa que tenha um efeito 
verificável) e execute o programa.

Se a verificação do ponto central for incorreta, deve haver um problema na 
primeira metade do programa. Se for correta, o problema está na segunda
metade.

Cada vez que executar uma verificação assim, divida ao meio o número de 
linhas a serem verificadas. Depois de seis passos (que é menos de 100), 
você teria menos de uma ou duas linhas do código para verificar, pelo menos
em teoria.

Na prática, nem sempre é claro o que representa o “meio do programa” e nem 
sempre é possível verificá-lo. Não faz sentido contar linhas e encontrar o 
ponto central exato. Em vez disso, pense em lugares no programa onde poderia 
haver erros e lugares onde é fácil inserir um ponto de verificação. Então 
escolha um lugar onde as possibilidades são basicamente as mesmas de que o 
defeito esteja antes ou depois da verificação.

EXERCÍCIOS

Exercício 7.1

def mysqrt(a):
    x = int(input("Qual a estimativa inicial?"))
    count = 0
    while True:
        count = count + 1
        print(x)
        y = (x + a/x) / 2
        if y == x:
            print('Number of iterations: ',count)
            break
        x = y
mysqrt(9)

Exercício 7.2

import math
def eval_loop():
    Done = "Done"
    while True:
        a = input("Digite uma expressão para avaliar ou 'Done' para encerrar: ")
        print(eval(a))
        if a == Done:
            break
eval_loop()

Exercício 7.3

import math

def estimate_pi():
	sum = 0
	epsilon = math.pow(10, -15)
	k = 0
	i = 1 #initialize i, the value doesn't matter
	while i > epsilon:
		i = (math.factorial(4*k) * (1103 + 26390 * k)) / (math.pow((math.factorial(k)), 4) * math.pow(396, 4*k) )
		sum += i
		k += 1 #!important
	inverse = 2 * math.sqrt(2) * sum / 9801
	return 1/inverse
	
print estimate_pi()
print math.pi
print estimate_pi() - math.pi
"""
