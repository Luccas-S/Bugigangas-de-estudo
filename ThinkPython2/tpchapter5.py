"""
===Condicionais e Recursividade===

DIVISÃO PELO PISO E MÓDULO

"O operador de divisão pelo piso,
"//", divide dois números e arredonda o resultado para 
um número inteiro para baixo."

Neste exemplo fazemos um cálculo para transformar os minutos em horas,
feito isso pegamos o restante de minutos e adicionamos ao número de horas.

minutes = 105
hours = minutes // 60

remainder = minutes % 60

print(hours, ":", remainder)

Operador Módulo = %.
"O operador módulo é mais útil do que parece. 
Por exemplo, é possível verificar se um número é divisível por outro
-> se x % y for zero, então x é divisível por y.

Além disso, você pode extrair o dígito ou dígitos mais à direita de um número. 
Por exemplo, x % 10 produz o dígito mais à direita de x (na base 10). 
Da mesma forma x % 100 produz os dois últimos dígitos."

EXPRESSÕES BOOLEANAS

"Uma expressão booleana é uma expressão que pode ser verdadeira ou falsa. 
Os exemplos seguintes usam o operador ==, 
que compara dois operandos e produz True se forem iguais 
e False se não forem"(Interação que ocorre no console do python)

>>>5 == 5
True
>>>5 == 6
False

True e False são valores especiais de tipo bool.

Além do "==", outros operadores relacionais são:

    "!=" - Diferente de.
    ">" - Maior que.
    "<" - Menor que.
    ">=" - Maior ou igual a.
    "<=" - Menor ou igual a.

OPERADORES LÓGICOS

Existem três operadores lógicos: and, or e not. Cujo significado semântico
é parecido com o significado real em Inglês.

No caso do "and" podemos dar o seguinte exemplo: 
"x> 0 and x <10" só é verdade se x for maior que 0 e menor que 10.

Um exemplo com "or" pode ser o seguinte: 
"n%2 == 0 or n%3 == 0" é verdadeiro se uma 
das ou ambas as condições forem verdadeiras, no caso, se o 
número for divisível por 2 ou 3.

Por último, "not" nega uma expressão booleana, ou seja, "not(x > y)" 
é verdade se x > y for falso(se x for menor que ou igual a y).

"Falando estritamente, os operandos dos operadores lógicos devem ser 
expressões booleanas, mas o Python não é muito estrito. 
Qualquer número que não seja zero é interpretado como True."

EXECUÇÃO CONDICIONAL

Execuções condicionais são partes do programa que verificam uma condição
e baseada nela, procede a execução de maneiras diferentes, mudando o
comportamento do programa de acordo. A maneira mais básica de criar uma
instrução condicional é o "if". O exemplo abaixo denota como um if básico
funciona direto no console do Python:

if x > 0:
    print('x is positive')

Rápidamente podemos perceber que no exemplo usado temos uma
expressão booleana, esta é a condição, se verdadeira, a instrução
abaixo do if é executada, caso contrário nada acontece.

Uma instrução if tem uma estrutura muito semelhante a uma definição
de função com cabeçalho e corpo indentado. Esse tipo de instrução é
uma instrução composta.

"Não há limite para o número de instruções que podem aparecer no corpo, 
mas deve haver pelo menos uma. Ocasionalmente, é útil ter um corpo 
sem instruções (normalmente como um espaço reservado para código que 
ainda não foi escrito). 
Neste caso, você pode usar a instrução pass, que não faz nada."

if x < 0:
    pass

EXECUÇÃO ALTERNATIVA

Outra forma de usar uma instrução if é usando uma execução alternativa,
onde existem duas(ou mais) possibilidades e a condição determina qual será
executada, segue exemplo abaixo:

if x % 2 == 0
    print('X is even')
else:
    print('X is odd')

No exemplo acima a instrução tem como condição o resto da divisão de X por 2,
caso o resto seja igual a 0, a execução do código vai devolver um print
dizendo que X é par. Caso contrário, a execução vai devolver uma print
que diz que X é impar. Neste caso, a condição deve ser verdadeira ou falsa
e apenas uma das alternativas será executada. Cada alternativa possível
numa instrução if tem o nome de "branch", que são ramos diferentes no fluxo
de execução.

CONDICIONAIS ENCADEADAS

Em uma instrução condicional existe a chance de termos que lidar com
multiplas possibilidades de execução do código e precisamos de mais branches.
No exemplo a seguir podemos ver uma operação de computação expressada de
forma que teremos uma condicional encadeada:

if x < y:
    print('X is less than Y')
elif x > y:
    print('X is greater than Y')
else:
    print('X and Y are equal')

No exemplo acima usamos uma instrução chamada "elif", esta é uma abreviatura
da instrução "else if". Neste caso, mais uma vez apenas uma branch será
executada. Não existem limites para o número de instruções elif que
podem ser usadas. Se houver uma cláusula else, ela deve estar no fim, mas
não é preciso haver uma.

if choice == 'a':
    draw_a()
elif choice == 'b':
    draw_b()
elif choice == 'c':
    draw_c()

Neste caso vemos que cada condição da instrução if é verificada em ordem,
se a primeira for falsa, então o programa executa a próxima e a verifica e
assim por diante, quando uma for verdadeira, a branch será executada e o 
if é encerrado. Mesmo se mais de uma condição for verdadeira, só a primeira
branch verdadeira será executada.

CONDICIONAIS ANINHADAS

Uma condicional aninhada é uma instrução if indentada 
dentro de outro if que é executada caso uma condição específica 
do if em que reside for verdadeira. Podemos escrever a estrutura descrita
da seguinte maneira:

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

A condicional "primária" contém duas branches, a primeira contém uma
instrução simples, já a segunda branch contém outra instrução if que
tem outros dois ramos que serão verificados.

Existem formas de evitar essa estrutura aninhada usando operadores lógicos.

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

"A instrução print só é executada se a colocarmos depois de ambas as 
condicionais, então podemos obter o mesmo efeito com o operador and."

if 0 < x and x < 10:
    print('x is a positive single-digit number.')

"Para este tipo de condição, o Python oferece uma opção mais concisa."

if 0 < x < 10:
    print('x is a positive single-digit number.')

RECURSIVIDADE

No Python3 podemos utilizar o recurso de chamar uma função em outra função ou ainda uma
função chamar a si própria. Veja um exemplo de uma estrutura que usa recursividade:

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

Nesta estrutura, observamos que se o parâmetro "n" for igual ou menor que 0, a função printa
a palavra "Blastoff!", caso contrário, a saída será o próprio "n" sendo exibido no console
e então a função chama a si mesma usando "n-1" como argumento, e o processo continua até que
a condição préviamente dita seja atingida. O resultado esperado de chamar a função da seguinte
forma "countdown(3)" será algo como isto:

3
2
1
Blastoff!

Funções que chamam outras ou a si mesmas são ditas recursivas.

Podemos escrever outro exemplo de uma estrutura que exibe uma string n vezes:

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

Se n <= 0 a instrução return causa a saída da função. 
O fluxo de execução volta imediatamente a quem fez a chamada, 
e as linhas restantes da função não são executadas.

O resto da função é similar à countdown: ela mostra s e então chama a si mesma para mostrar s 
mais n-1 vezes. Então o número de linhas da saída é 1 + (n - 1), até chegar a n.

Para exemplos simples como esse, provavelmente é mais fácil usar um loop for. 
Mais adiante veremos exemplos que são difíceis de escrever com um loop for e 
fáceis de escrever com recursividade, então é bom começar cedo.

DIAGRAMAS DA PILHA PARA FUNÇÕES RECURSIVAS

Anteriormente na página 55 introduzimos o conceito de "Diagramas da Pilha", usamos um diagrama
da pilha para representar o estado de um programa durante uma chamada de função. Podemos
usar o mesmo tipo de diagrama para ajudar a interpretar uma função recursiva.

Cada vez que uma função é chamada, o Python cria um frame para conter as 
variáveis locais e parâmetros da função. Para uma função recursiva, pode haver mais de um 
frame na pilha ao mesmo tempo.

RECURSIVIDADE INFINITA

Para os casos onde a recursividade nunca atinge um caso-base, a mesma continuará fazendo 
chamadas recursivas para sempre, neste caso o programa nunca termina a execução. Este fenômeno
tem o nome de recursividade infinita e em praticamente todos os casos não é uma boa ideia.
Abaixo segue exemplo de um programa que apesar de mínimo em tamanho, tem recursividade infinita:

def recurse():
    recurse()

Na grande maioria dos ambientes de programação, um programa com recursividade infinita não é
de fato executado para sempre. O Python exibe uma mensagem de erro quando o limite da stack é
atingido. Segue exemplo do erro:

  File "<stdin>", line 2, in recurse
  File "<stdin>", line 2, in recurse
  File "<stdin>", line 2, in recurse
                  .
                  .
                  .
  File "<stdin>", line 2, in recurse
RuntimeError: Maximum recursion depth exceeded

Este traceback é um pouco maior que o que vimos no capítulo anterior. 
Quando o erro ocorre, há mil frames de recurse na pilha!

Se você escrever em recursividade infinita por engano, confira se a sua 
função tem um caso-base que não faz uma chamada recursiva. 
E se houver um caso-base, verifique se você vai mesmo atingi-lo.

ENTRADA DE TECLADO



"""
