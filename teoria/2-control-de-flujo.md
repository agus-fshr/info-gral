# Control de Flujo

En la parte anterior `2-primeros-pasos` aprendiste que es una variable y como realizar algunas operaciones matematicas basicas en Python. Si bien esto es util, vas a ver rapidamente que es aburrido. Hasta el momento, no tenemos ninguna manera de hacer que nuestro programa tome decisiones por su cuenta, ninguna manera de cubrir diferentes casos o posibilidades. Para esto, vamos a aprender a manejar expresiones condicionales. En particular, vamos a ver como se usa el `if/else`. *Si, ya se que a partir de la version 3.10.5 agregaron un tipo de switch-case pero no viene al caso*.

La sintaxis para un `if/else` es la siguiente.

```Python 
if condicion:
    CODIGO 1
else:
    CODIGO 2
```

Vamos a ver que significa esto. `condicion` es la condicion que se tiene que cumplir para que el `if` se active y ejecute `CODIGO 1`. Si `condicion` no resulta ser verdadera, entonces se activa el `else` y se ejecuta el `CODIGO 2`. Para darte algo mas concreto, vamos a ver un ejemplo.

```Python
a = 10
b = 5
if a > b:
    print('A')
else:
    print('B')
```

Aca, lo importante es darse cuenta que `a > b` es una expresion que solamente puede ser o verdadera o falsa, no es un numero. Se dice que es un valor booleano. En este ejemplo tambien aparece algo que hasta ahora no viste... un `print()`. `print()` es una funcion que toma lo que esta entre los parentesis y lo muestra en pantalla (si no codeaste una interfaz grafica, seguramente estes corriendo tus programas en algun tipo de terminal, asi que ahi vas a ver el texto). Entre comillas se pone texto para que muestre exactamente lo que tipeas pero tambien podes poner nombres de variables para que muestre el valor de las variables.

## Unos detalles mas sobre el `if`
No siempre es necesario tener un `else` con cada `if`. De hecho, en muchos casos puede ser mejor no tenerlo. Otra cosa que puede pasar es que no nos alcance con solamente un `if` y un `else`. Para estos casos existe el llamado `elif`. Como el nombre lo indica, es una mezcla de `else` e `if`. Vamos a ver como funciona con un ejemplo.

```Python
a = 2
if a == 1:
    print('Uno!')
elif a == 2:
    print('Dos!')
else:
    print('No se :(')
```

Como te daras cuenta, pueden ser bastante comodos los `elif`. Quizas te este llamando la atencion el `==`. Vamos a aclararlo ahora asi no tenemos problemas en el futuro. En Python (y en la mayor parte de los lenguajes de programacion) hay que hacer una distincion muy importante en lo que significa el "igual". Una cosa es asignacion, otra cosa es equivalencia y otra cosa muy distinta es identidad. Para asignar valores, como cuando estamos definiendo una variable, usamos el `=`. Cuando queremos preguntar si una cosa tiene el mismo valor que otra, como en la condicion de un `if`, usamos `==`. Finalmente, el tema de la identidad es un poco avanzado asi que no quiero entrar en detalles, pero muy superficialmente podriamos decir que dos cosas son identicas sin existen en el mismo lugar al mismo tiempo, es decir, que cuando modifico una, ni siquiera es que estoy modificando la otra, sino que son la misma, entonces, obviamente, se ve modificada tambien (es confuso, imaginate que vos y tu amigo Juan tienen un amigo en comun que vos conoces con el nombre Julio, pero Juan lo conoce como Jaime. De alguna manera se enteran de que Julio/Jaime se corta el pelo. Ustedes lo llaman de manera distinta, pero estan todos de acuerdo en que Julio/Jaime se corto el pelo. Julio no es igual a Jaime, ni son equivalentes. Son identicos, la misma persona!).

# Entrada de Usuarios
Esto de control de flujo esta buenisimo, nos deja tener un programa que esta preparado para considerar diferentes casos de resultados pero... como vamos a tener diferentes casos si hasta ahora nada de lo que hacemos es desconocido. Todos los valores que le llegan a nuestro programa los estamos poniendo nosotros. Vamos a ver ahora como podemos tomar entrada de un usuario. Esto va a incrementar enormemente la utilidad de nuestros programas.

Python, siendo uno de los lenguajes mas comodos del universo, nos da una funcion que se encarga de todo esto por nosotros. Se llama `input()` y en seguida vamos a ver como se usa.

```Python
nombre = input("Ingrese su nombre: ")
```

Bien, vamos a ver que paso ahi. Lo que esta entre parentesis es un mensaje que se muestra en la terminal, a continuacion el usuario va a ingresar su nombre y debe presionar `enter` para que el programa lea lo que ingresa. Y, al escribir `nombre = input()` estamos haciendo que el resultado de nuestro llamado a la funcion `input()` quede guardado en la variable `nombre`. Aca viene un tema que muchos olvidan pero que se adquiere con costumbre.

Si te acordas de las primeras cosas que aprendiste, todas las variables tienen un tipo de dato. Cuando poniamps un numero o texto o cualquier cosa explicita resultaba bastante obvio el tipo de dato. Pero, podrias decir cual es el tipo de dato de `nombre` en este programa? No es tan obvio. En general, las funciones devuelven algun resultado. Para poder hacer esto, ese resultado que devuelven tiene que tener un tipo de dato que define el que programa la funcion. En el caso de la funcion `input()` es siempre un `string`.

Seguramente en este momento te estes preguntando de que te sirve para tomar datos con valores numeros si siempre es un `string`. Gran pregunta, pero eso tambien lo resolvieron los creados de Python. Aca vamos a ver un tema de programacion que es super importante y basico pero que aun asi ha logrado confundir a muchos. Es el tema de los _casteos_. Esta palabra viene de _cast_ en ingles y tiene que ver con convertir algo de un tipo de dato a otro. Por ejemplo, el `string` "45" no es lo mismo que el `int` 45. Uno es un par de caracteres alfanumericos sin valor matematico y que no sirve para operar, mientras que el otro es un numero entero. Si hacemos `input()` y nos pasan como valor "45", vamos a tener que pasarlo a `int`. El casteo se hace de la siguiente manera `int("45")`. Ahora, vamos a ver como se hace con el input, es bastante intuitivo.
```Python
edad = int(input("Ingrese su edad: "))
```

Tambien podemos castear de `int` a `string` y entre practicamente todos los tipos de datos. El unico que no es con su propio nombre de tipo de dato (como `int`, que para castear a `int` hacemos `int()`) es el `string`. Para el `string` se castea haciendo `str()`.

Creo que con esto ya tenemos suficiente, asi que nos vemos en `4-atando-cabos-sueltos.md` para terminar de cerrar un par de cositas pendientes.
