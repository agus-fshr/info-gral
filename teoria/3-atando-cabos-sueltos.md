En esta seccion voy a ver si termino de explicar o desarrollar un par de cosas que pueden haber quedado colgadas o que omiti para poder ir al grano con otros temas. No por esto es menos importantes que otras partes asi que igualmente te recomiendo que la leas.

Para ahorrarte tiempo, voy a tratar de describirlas con algun simbolo que ordene por prioridad. Las que tengan numero mas bajo van a ser de prioridad alta. Esto quiere decir que considero que deberias leerlas (en realidad, estaria bueno que leas todas, pero si vas a empezar a recortar, estas no las saltees). Las de numero mas alto van a ser de menor priodidad. Esto quiere decir que vas a poder vivir en paz sin saberlo y probablemente no te traiga muchos problemas, por lo menos no seguido.

# Asignacion (I)
Cuando asignamos valor a variables, quizas se te ocurrio en lugar de hacer `a=2`, `2=a`. Primero, no. Segundo, esto no funciona porque en programacion hacemos una distincion entre valores que van a izquierda de un igual (lvalues) y valores que van a derecha de un igual (rvalues). Una expresion definida como lo es un numero entero, siempre va a ir a la derecha de un `=`. De la misma manera, el nombre de una variable o de algo que recibe un valor, va a ir siempre a la izquiera. Si te sirve, lo podes pensar como si en lugar de `a=2` fuera `a<-2`.

# Evaluacion de Expresiones

## Combinando Expresiones (I)

A medida que uses mas las expresiones logicas y condiciones de `if`s, te vas a ir acostumbrando a la forma de pensar y vas a darte cuenta de que te falta algo. Hay algo que no mencione hasta ahora y que es super util. Podemos combinar expresiones logicas usando `and`, `or` y `not` (el `not` tambien se puede reemplzar por `!`).

Supongamos que queremos que la variable `x` pertenezca al intervalo (2,5) o que no perteneza al intervalo (0,1]. Podriamos expresar esto como `(2<x and x<5) or not (0<x and x<=1)`. Por las didas, los parentesis estan para que el `or` agarre ambos `and`s y no solamente las expresiones inmediatamente mas cercanas.

## Lazy (III)
Todas las expresiones en Python se evaluan de manera *lazy*. Esto quiere decir que dejan de evaluarse en el momento que su valor queda definido. Es super entendible que aun no te haya quedado claro asi que te voy a dar un ejemplo con el que seguro entendes.

Supongamos que tenes que evaluar la expresion A y B y C. Claramente, solo va a ser verdadera cuanto A, B y C sean verdaderas a la vez. Python va a ir en orden una por una, pero ni bien vea que alguna es falsa, va a dejar de evaluar todas las otras porque ya sabe que el resultado nunca va a ser verdadero. Imaginate que te vas a juntar con tus amigas para salir a bailar pero no queres que ninguna quede afuera, asi que solo deciden salir si todas pueden. Ni bien alguna de tus amigas te dice que no va a poder ir, dejas de preguntarle al resto, porque ya sabes que no van a poder ir todas. Python hace lo mismo.

## Boolean Casting (II)
Los numeros se pueden castear a booleanos. De hecho, cuando se evaluan expresiones booleanas (como en la condicion de un `if`) esto sucede de manera implicita. Ni me voy a gastar en explicar en terminos que confunden, voy a dar un ejemplo y te prometo que vas a entender todo.

Supongamos que tenemos una fabrica con distintos sectores y que en distintas variables vamos a contar la cantidad de distintos tipos de errores. Vamos a querer detener la fabrica si hay un error de cualquier tipo. Hay dos maneras de hacer esto.

**Manera 1**
```Python
if !(error_tipo_1 == 0 and error_tipo_2 == 0 and error_tipo_3 == 0):
    detener()
```

Manera 2
```Python
if !(error_tipo_1 + error_tipo_2 + error_tipo_3):
    detener()
```

Funcionan de la misma manera, pero la segunda es mucho mas legible, corta y comoda. Lo fundamental a entender es que `0` casteado a `bool` es `False` y que cualquier otro numero casteado a `bool` es `True`.
