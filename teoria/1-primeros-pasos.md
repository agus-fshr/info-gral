# Operaciones Basicas
Bueno, no deberia ser ninguna sorpresa que entre las cosas mas basicas que podes hacer en Python esta... hacer cuentas.

Si, ya se que la re baja pero es importante saber estas cosas para poder expresarnos mejor a la hora de decirle que hacer a la compu.

Voy a hacer mi mejor esfuerzo por sacarnos de encima esta seccion en el menor tiempo posible, porque me parece un bodrio y es algo realmente muy dificil de no aprender.

- La suma es igual que siempre, con el operador `+`
- La resta, tambien es igual que siempre, con el operador `-`
- El producto se hace con el operador `*`
- Lla potencia se hace con el operador `**`. Por si no queda, claro, "dos al cubo" seria `2**3`
- La division se hace con el operador `/`
y aca se pone divertido para algunos...


Dijimos que la division se hace con `/` pero hay dos operaciones mas relacionadas con la division. Una de ellas es la division entera y la otra se llama modulo o resto (no, no es el modulo que estas pensando).

La division entera es exactamente lo que parece. Es una division que da por resultado un numero entero. Como lo hace? Si da con coma, corta todo lo que venga despues de la coma y lo ignora. Doy un ejemplo para que se entienda mejor.

`2/5` da `2.5`, mientras que `2//5` da `2`.

La otra operacion de la que hablamos es mucho mas interesante. Esta nos da el resto de una division, o, si vienen de informatica, nos da la congruencia. De nuevo, se va a entender mejor con un ejemplo.

`2%5` da `1`. Esto es porque `5 = 2\*2 + 1`. `1` es el resto de la division. Esto es super poderoso para, por ejemplo, determinar si un numero es divisible por otro. Cuando `a` va a ser divisible por `b`? Facil. Cuando `a%b` nos de cero.

## Pausa para hacer cosas mas divertidas
Abri su terminal. Si estas en mac o Linux ya deberias saber, para Windows, hace `Win+R`, tipea "cmd" y mete enter.

Ahora seguimos con los pasos que son iguales para todos. En la terminal tipea `python` y apreta enter. Ahora estas en una terminal de python. Aca podes escribir sentencias (comandos, aproximadamente) de python y ni bien toques enter se van a ejectuar. Aprovecha esto para testar algunas expresiones matematicas y ver que funcionen.

Ya que estamos, trata de combinar expresiones matematicas y usa parentesis. Vas a ver que sigue todas las reglas de orden de operaciones de matematica. Obviamente esto es a proposito. Los lenguajes de programacion tienen la funcion de ayudarnos a expresar nuestros problemas (y soluciones) a la computadora. Vas a ver que tienen muchas cosas que son comodas y que todo esta hecho con el fin de hacernos la vida mas facil (aunque a veces cueste creerlo).

# Variables
Este concepto, por algun motivo, confunde mucho a personas que estan programando por primera vez, aunque no tiene por que ser asi. Las variables de las que hablamos en programacion no tienen nada de distinto con las variables que tratamos en matematica. Veamos que significa esto...

Una variable en programacion es como si fuera una caja que almacena informacion. Tienen un nombre, para que podamos llamarlas desde nuestro programa, y viven en algun lugar de nuestra computadora (en Python, no nos tenemos que preocupar por esto pero en otros lenguajes vamos a tener que pedirle a la computadora que reserve memoria en la RAM para nuestras variables y decirle donde y como guardarlas).

La particularidad que tienen las variables en programacion que confunde a algunas personas es que tienen un **tipo de dato**. Esto es como decir que el numero o valor que toma una variable pertenece a cierto conjunto de numeros. Una variable puede almacenar un numero entero (`int`), numero decimal (`float`), cadena de caracteres (`string`), valor de verdad logico (`bool` de booleano) y por ahora lo dejamos ahi. Existen otros tipos de datos pero en lineas generales se pueden expresar como combinaciones de estos.

En Python crear una variable y darle un valor es extremadamente sencillo. Se hace de la siguiente manera.
```Python
x = 1
y = 2.5
z = "hola"
```
En el ejemplo de arriba creamos 3 variables. La variable `x` con valor `1` y tipo de dato `int`, la variable `y` con valor `2.5` y tipo de dato `float` y la variable `z` con valor `"hola"` y tipo de dato `string`.

Fijate que en ningun momento le especifique al programa cual era el tipo de dato que queria usar. Esto es una comodidad (pero tambien puede ser una desventaja para algunos, es una espada de doble filo, porque nos saca un poco de control y nos malcria) que tiene Python. El lenguaje determina por su cuenta el tipo de dato que debe usar para la variable segun el valor que nosotros le asignamos.

Ahora que introdujimos el concepto de variable y de tipo de dato podemos empezar a hacer cosas muy divertidas. Te recomiendo fuertemente que vuelvas a a terminal de Python e intentes por tu cuenta operar como antes pero incluyendo ahora variables y distintos tipos de dato. A continuacion te dejo un par de cosas que deberias probar.
- sumar cadenas de texto
- asignarle a una variable su propio valor
- asignarle a una variable su propio valor pero modificado por otra operacion
- multiplicar cadenas de texto por un numero

Tip: si tipeas el nombre de una variable en la terminal y pones enter, te muestra el valor de la variable.
