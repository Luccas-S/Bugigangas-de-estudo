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



"""