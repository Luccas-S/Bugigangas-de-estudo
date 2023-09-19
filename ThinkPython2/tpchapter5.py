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
e baseada nela, procede 
"""
