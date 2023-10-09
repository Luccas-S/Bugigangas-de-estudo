"""
===Funções com Resultado===

"Muitas das funções do Python que usamos, como as matemáticas, 
produzem valores de retorno. Mas as funções que escrevemos até 
agora são todas nulas: têm um efeito, como exibir um valor ou mover 
uma tartaruga, mas não têm um valor de retorno. 
Neste capítulo você aprenderá a escrever funções com resultados."

VALORES DE RETORNO

Sempre que temos uma chamada de função geramos um valor de retorno,
este que normalmente usamos para atribuir a uma variável ou como parte de uma
expressão.

e = math.exp(1.0)
height = radius * math.sin(radians)

Até o momento, todas as funções que descrevemos são nulas,
não tem valores de retorno, ou, para ser mais exato, o retorno foi none.

Neste capítulo vamos adentrar em como escrever funções com retorno.
O primeiro exemplo é area, que desvolve a área de um círculo com o raio
dado:

def area(radius):
    a = math.pi * radius**2
    return a

Já usamos a instrução return antes, mas neste caso, como a função tem
resultado, ela inclui uma expressão. A instrução significa algo como:
"Volte desta função e use a seguinte expressão como valor de retorno.".

No caso do exemplo usado, a expressão pode ser desnecessáriamente
longa/complicada, poderíamos escrever de outra forma para tornar mais
concisa:

def area(radius):
    return math.pi * radius**2

Da mesma forma que o exemplo acima é mais conciso, sem o uso da variável
temporária "a", a depuração do mesmo se torna mais complicada.

Por vezes é útil usar várias instruções de retorno, uma em cada ramo
de uma condicional por exemplo.

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

No exemplo acima, já que cada instrução return está em um ramo diferente
de uma condicional, apenas uma será executada. Assim que uma das duas
for executada, a função termina sem executar mais nenhum código. Código que
está abaixo de uma instrução return é chamado de código morto.

"Em uma função com resultado, é uma boa ideia garantir que cada caminho
possível pelo programa atinja uma instrução return. Por exemplo:"

def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x

Este exemplo está incorreto, se X for igual a 0, nenhum ramo da condicional
é verdade, logo nunca chegamos a uma instrução return, e se não atinjimos
o return, o retorno será none.

>>> absolute_value(0)
None

def compare(x, y):

    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

DESENVOLVIMENTO INCREMENTAL

Conforme você desenvolver funções mais longas, pode ser que passe mais
tempo as depurando.

Para lidar com esse tipo cada vez mais extenso de programa, você pode
usar o recurso do desenvolvimento incremental. A intenção ao utilizar desenvolvimento
incremental é evadir sessões longas de depuração ao mesmo tempo que diminui a margem de erro
já que partes menores do código são adicionadas de cada vez.

Como um exemplo, vamos supor que você queira encontrar a distância entre dois pontos dados 
pelas coordenadas (x1, y1) e(x2, y2). Pelo teorema de Pitágoras, a distância é igual a
raiz de (x2 - x1)² + (y2 - y1)²

O primeiro passo é pensar como uma função distance deveria ser no Python. 
Em outras palavras, quais são as entradas (parâmetros) e qual é a saída (valor de retorno)?

Nesse caso, as entradas são dois pontos que você pode representar usando quatro números. 
O valor de retorno é a distância representada por um valor de ponto flutuante.

Imediatamente, é possível escrever um rascunho da função:

def distance(x1, y1, x2, y2):
    return 0.0

Claro que esta versão não calcula distâncias; sempre retorna zero. Mas está sintaticamente 
correta, e pode ser executada, o que significa que você pode testá-la antes de torná-la 
mais complicada.

Para testar a nova função, chame-a com argumentos de amostra:

>>> distance(1, 2, 4, 6)
0.0

Escolhi esses valores para que a distância horizontal seja 3 e a distância vertical, 4; 
assim, o resultado final é 5, a hipotenusa de um triângulo 3-4-5. 
Ao testar uma função, é útil saber a resposta certa.

Neste ponto confirmamos que a função está sintaticamente correta, e podemos começar a 
acrescentar código ao corpo. Um próximo passo razoável é encontrar as diferenças 
x2 - x1 e y2 - y1. A próxima versão guarda esses valores em variáveis temporárias e os exibe:

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)
    print('dy is', dy)
    return 0.0

Se a função estiver funcionando, deve exibir dx is 3 e dy is 4. Nesse caso sabemos que a 
função está recebendo os argumentos corretos e executando o primeiro cálculo acertadamente. 
Se não, há poucas linhas para verificar.

Depois calculamos a soma dos quadrados de dx e dy:

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    print('dsquared is: ', dsquared)
    return 0.0

Nesta etapa você executaria o programa mais uma vez e verificaria a saída (que deve ser 25). 
Finalmente, pode usar math.sqrt para calcular e devolver o resultado:

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

Se funcionar corretamente, pronto. Senão, uma ideia é exibir o valor result antes da 
instrução de retorno.

Podemos notar que a versão final não exibe nada quando executada; apenas retorna um valor.
Apesar de úteis para depuração, as intruções que usamos não precisam ser exibidas na versão
final, assim que a depuração acaba, o ideal seria remover as exibições desnecessárias assim
que o funcionamento do programa for conferido. Códigos dessa estirpe são chamados de
scaffolding(andaime) porque são úteis para construir e depurar um programa, mas não fazem
parte do produto final. O tamanho das parcelas de código para depurar podem aumentar com
a experiência do programador, independente da experiência, o desenvolvimento incremental
economiza muito tempo de depuração.

Os principais aspectos do processo são:

1 - Comece com um programa que funcione e faça pequenas alterações incrementais. 
Se houver um erro em qualquer ponto, será bem mais fácil encontrá-lo.

2 - Use variáveis para guardar valores intermediários, assim poderá exibi-los e verificá-los.

3 - Uma vez que o programa esteja funcionando, você pode querer remover uma parte do scaffolding
ou consolidar várias instruções em expressões compostas, mas apenas se isso não tornar 
o programa difícil de ler.

COMPOSIÇÃO

Já vimos antes que podemos chamar uma função dentro de outra, podemos exemplificar isso com
o seguinte raciocínio e exemplos:

Escrevemos uma função que recebe dois pontos, o centro do círculo e um ponto no perímetro para
calcular a área do círculo. Supondo que o ponto central esteja armazenado nas variáveis xc e yc
enquanto que o perímetro está em xp e yp. Devemos primeiro encontrar o raio do círculo
(distância entre os dois pontos). Com isso, escrevemos a função distance, que faz isto:

radius = distance(xc, yc, xp, yp)

A próxima etapa é encontrar a área de um círculo com aquele raio, escrevemos isso também:

result = area(radius)

Quando encapsulamos esses passos numa função, obtemos:

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

Variáveis temporárias como a radius e a result são úteis para desenvolvimento e depuração,
uma vez que o programa esteja funcionando podemos torná-lo mais conciso compondo chamadas
de função:

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

FUNÇÕES BOOLEANAS

O retorno de funções definidas pode ser booleano, isto é, verdadeiro ou falso, resultado este
que será utilizado em outras partes do código, um uso interessante desse artifício é esconder
testes complicados dentro de funções como no exemplo a seguir:

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

É comum e comodo dar nomes de perguntas para funções booleanas, isso permite uma compreensão
direta do que a função faz e já da algum contexto para o tipo de retorno dessa função.

>>> is_divisible(6, 4)
False
>>> is_divisible(6, 3)
True

O resultado do operador "==" é um booleano, logo podemos escrever a mesma função de forma
mais concisa, retornando-o diretamente.

def is_divisible(x, y):
    return x % y == 0

Frequentemente as funções booleanas são usadas em conjunto à instruções adicionais.

if is_divisible(x, y):
    print('x is divisible by y')

Pode ser tentador escrever algo assim:

if is_divisible(x, y) == True:
    print('x is divisible by y')

Porém, a comparação extra neste caso se mostra desnecessária.

MAIS RECURSIVIDADE

"Cobrimos apenas um pequeno subconjunto do Python, mas talvez seja bom você saber que este 
subconjunto é uma linguagem de programação completa, ou seja, qualquer coisa que possa ser 
calculada pode ser expressa nesta linguagem. 
Qualquer programa que já foi escrito pode ser reescrito apenas com os recursos da linguagem 
que você aprendeu até agora (na verdade, seria preciso alguns comandos para dispositivos de 
controle como mouse, discos etc., mas isso é tudo).

Comprovar esta declaração é um exercício nada trivial realizado pela primeira vez por Alan Turing
, um dos primeiros cientistas da computação (alguns diriam que ele foi matemático, mas muitos 
dos primeiros cientistas da computação começaram como matemáticos). Assim, é conhecida como a 
Tese de Turing. Para uma exposição mais completa (e exata) da Tese de Turing, recomendo o 
livro de Michael Sipser, Introduction to the Theory of Computation (Introdução à teoria da 
computação, Course Technology, 2012).

Para dar uma ideia do que podemos fazer com as ferramentas que aprendeu até agora, avaliaremos 
algumas funções matemáticas definidas recursivamente. 
Uma definição recursiva é semelhante a uma definição circular, no sentido de que a definição 
contém uma referência à coisa que é definida. Uma definição realmente circular não é muito 
útil:"

-vorpal
    Adjetivo usado para descrever algo que é vorpal.

Ver uma definição realmente circular como essa num dicionário pode ser frustrante, enquanto
que procurar a definição da função fatorial(representada pelo símbolo "!"), encontrará algo
assim:

0! = 1
n! = n·(n - 1)!

Na definição acima vemos que o fatorial de 0 é 1, e o fatorial de qualquer outro valor n será
n multiplicado pelo fatorial de n - 1.

"Então 3! é 3 vezes 2!, que é 2 vezes 1!, que é 1 vez 0!. Juntando tudo, 3! é igual a 3 
vezes 2 vezes 1 vezes 1, que é 6."

Quando você consegue escrever uma definição recursiva de qualquer coisa você então também pode
a avaliar usando Python. O primeiro passo seria definir que parâmetros ela terá e neste caso
fica claro que factorial deve receber um número inteiro:

def factorial(n):

Se o argumento for 0, tudo que precisamos fazer é retornar 1:

def factorial(n):
    if n == 0:
        return 1

Quando o argumento não é 0 que as coisas ficam interessantes, daí começamos a de fato avaliar
a definição recursiva, no caso de um fatorial precisamos usar de uma chamada recursiva para
encontrar o fatorial de n - 1 e então multiplicá-lo por n:

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

O fluxo de execução deste programa é semelhante ao fluxo de countdown em “Recursividade”, 
na página 81. Se chamarmos factorial com o valor 3:

Como 3 não é 0, tomamos o segundo ramo e calculamos o fatorial de n-1…

    Como 2 não é 0, tomamos o segundo ramo e calculamos o fatorial de n-1…

        Como 1 não é 0, tomamos o segundo ramo e calculamos o fatorial de n-1…

            Como 0 é igual a 0, tomamos o primeiro ramo e devolvemos 1 sem fazer mais chamadas recursivas.

        O valor de retorno, 1, é multiplicado por n, que é 1, e o resultado é devolvido.

    O valor de retorno, 1, é multiplicado por n, que é 2, e o resultado é devolvido.

O valor devolvido (2) é multiplicado por n, que é 3, e o resultado, 6, torna-se o valor devolvido pela chamada de função que começou o processo inteiro.
        
SALTO DE FÉ

Apesar de ser a forma mais comum de ler programas, seguir o fluxo de execução pode ser 
trabalhoso demais, logo, mesmo que de forma inconsciente, usamos muito o chamado "leap of faith"
ou salto de fé, é o princípio de que confiamos que uma parte do código funcione por "fé"
em quem a programou, logo não precisamos ler o corpo desta parte do código, tomando como verdade
que esta parte funciona, eliminando a necessidade de examinar e depurar partes muitas vezes
complexas de código. O fato é que usamos isso quase sempre sem nem mesmo perceber, um exemplo
é quando usamos funções integradas, nunca nos questionamos se "math.sqrt" funciona, confiamos
que sim, sem examinar o corpo dessa função. Primeiro de tudo ao ler um programa e o examinar
é confiar que o mesmo funcione como deveria, isso elimina grande parte do processo de leitura.

O mesmo princípio de salto de fé pode ser aplicado à programas recursivos; Quando chega à
chamada recursiva, em vez de só seguir o fluxo de execução, deve-se pressupor que a chamada
funcione e devolva o resultado correto e só então perguntar-se: "Supondo que eu possa encontrar
o fatorial de n - 1, posso calcular o fatorial de n?". Claro que pode, multiplicando por n.

Pode ser um pouco esdrúxulo supor préviamente que uma função funcione corretamente quando
sequer terminou de escrevê-la, mas é justamente por isso que se chama salto de fé!

MAIS UM EXEMPLO

Após o factorial, um exemplo tão comum quanto seria o Fibonacci, que tem a seguinte definição:

fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

Traduzindo para Python, Fibonacci pode ser avaliado da seguinte forma:

def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

Ao tentar seguir o fluxo de execução normalmente, mesmo com valores pequenos é visível que
rápidamente as coisas complicam. Quando seguimos o salto de fé e supomos que as duas chamadas
recursivas funcionam corretamente, é claro que vamos receber um resultado correto adicionando
elas juntas.

VERIFICAÇÃO DE TIPOS

Vejamos o que acontece se chamarmos factorial e usarmos 1.5 como argumento:

>>> factorial(1.5)
RuntimeError: Maximum recursion depth exceeded

Parece que se trata de uma recursão infinita, mas, por que isso acontece? Veja bem, a função
possuí um caso base quando n == 0. Vemos que neste caso n não é um número inteiro, logo perd-
emos o caso-base e recorremos infinitamente, o Python previne isso com um limite de recursão.

Quando temos a primeira chamada recursiva, o valor de n se torna 0.5, da segunda pra frente
o número fica negativo(-0.5), e se torna cada vez menor, mas nunca chegará a 0.

Temos então duas escolhas para resolver este problema, a primeira envolve generalizar a função
para trabalhar com números de ponto flutuante, tratando-se de uma função gamma, o que está 
além do escopo de Think Python 2.
A segunda opção envolve controlar o tipo de argumento que a função recebe, podemos usar a
função integrada isinstance para verificar o tipo de argumento. E vamos aproveitar para
verificar também se o argumento é positivo:

def factorial (n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

Vemos que agora a função tem um caso-base que engloba números não inteiros e números inteiros
negativos, em ambos os casos a função devolve uma mensagem de erro e retorna None, indicando
que algo deu errado:

>>> factorial('fred')
Factorial is only defined for integers.
None
>>> factorial(-2)
Factorial is not defined for negative integers.
None

Passando por ambas verificações saberemos que n é positivo ou zero, podendo comprovar que a 
recursividade termina.

Esse programa demonstra um padrão às vezes chamado de guardião. As duas primeiras condicionais
atuam como guardiãs, protegendo o código que segue de valores que poderiam causar um erro.
As guardiãs permitem comprovar a correção do código.

DEPURAÇÃO



"""