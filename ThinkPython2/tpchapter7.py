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



"""