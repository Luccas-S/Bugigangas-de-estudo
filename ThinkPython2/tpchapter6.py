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

Nesse caso, as entradas são dois pontos que você pode representar usando quatro números. O valor de retorno é a distância representada por um valor de ponto flutuante.

Imediatamente, é possível escrever um rascunho da função:

def distance(x1, y1, x2, y2):
    return 0.0
Claro que esta versão não calcula distâncias; sempre retorna zero. Mas está sintaticamente correta, e pode ser executada, o que significa que você pode testá-la antes de torná-la mais complicada.

Para testar a nova função, chame-a com argumentos de amostra:

>>> distance(1, 2, 4, 6)
0.0
Escolhi esses valores para que a distância horizontal seja 3 e a distância vertical, 4; assim, o resultado final é 5, a hipotenusa de um triângulo 3-4-5. Ao testar uma função, é útil saber a resposta certa.

Neste ponto confirmamos que a função está sintaticamente correta, e podemos começar a acrescentar código ao corpo. Um próximo passo razoável é encontrar as diferenças x2 − x1 e y2 − y1. A próxima versão guarda esses valores em variáveis temporárias e os exibe:

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)
    print('dy is', dy)
    return 0.0

"""