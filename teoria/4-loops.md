# Loops!

Este es un concepto extremadamente util y que no vas a lograr entender o dominar hasta que no lo uses un par de veces. Los loops o bucles son sentencias u operaciones que nos permiten ejecutar un bloque de codigo una cierta cantidad de veces que puede ser variable o fijo. Ahora vamos a conocer los dos bucles mas comunes y si queres aprender sobre otros los podes googlear, aunque con estos dos te va a alcanzar para la mayor parte de las cosas que quieras hacer en Python.

## `for` loops

Vamos a empezar con el loop `for`, el mas comun y simple de todos. Este permite ejecutar el codigo que esta dentro del mismo una cantidad fija de veces. Veamos la sintaxis

```Python
for x in range(0, 5):
    print("hola!")
```

En este ejemplo `x` es lo que se conoce como *iterador*. Es una variable que va a tomar un valor segun el numero de iteracion en que se encuentre en loop. Por las dudas, la iteracion es como la repeticion en la que estamos. `range(0,10)` es una sentencia que esta usando la funcion `range()` para tomar un rango de numeros entre 0 y 10. Entonces, lo que estamos haciendo con este loop es que `x` tome los valores entre 0 y 10 (sin contar el 10) y para cada uno de esos valores imprima el texto "hola!".

Inmediatamente podemos ver que esto es super util y que se parece bastante a la sumatoria que conoces de matematica! Sin el `for` seria muy dificil hacer cosas como aproximaciones por polinomios de Taylor en computadoras. Sin embargo, el `for` tiene funcionalidades mucho mas poderosas que vas a poder usar cuando aprendas a trabajar con listas. Por ahora, te anticipo que esa `x` (que en realidad no tiene por que llamarse asi, puede ser cualquier variable) no tiene por que ser un numero, y que el loop no tiene por que ser sobre una serie de numeros... puede ser cualquier conjunto de cosas!

Te dejo un ejemplo mas a ver si podes darte cuenta de que hace.

```Python
sum = 0

for num in range(0,101):
    sum += num

print(sum)
```

Bueno, estoy por revelar la respuesta asi que si no lo miraste todavia tenes tiempo........................ bueno se acabo. Lo que hace el codigo es sumar todos los enteros de 0 a 100 e imprimir el resultado de eso en la pantalla.



## `while` loops

Estos tienen la diferencia de que nos permiten ejecutar codigo mientras sea verdadera cierta expresion. Los podemos usar para repetir operaciones hasta que suceda o deje de suceder algo. El numero de iteraciones no es fijo. Te dejo un ejemplo, y como ya entendes a la perfeccion el `for`, no te va a costar entender esto.

```Python
x = 10
while x > 0:
    x -= 1
    print(x)
```

Aca podemos ver que la condicion es `x > 0`. Es decir, que el codigo indentado se ejecute mientras `x` sea mayor a cero. Cuando deje de serlo, se dejara de ejecutar ese bloque de codigo.
