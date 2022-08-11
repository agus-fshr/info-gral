# Por que programamos?
La programacion es una herramienta que nos permite resolver problemas variados. Estos pueden variar desde calcular cosas que antes no podiamos, simular diversas situaciones, automatizar tareas, estudiar enormes series de datos, entre muchas otras cosas. El denominador comun que tienen todos los progamas es que tienen el proposito de hacernos mas facil la vida. Un programa que vale la pena es uno que nos ahorra mucho mas tiempo del que nos tarda programarlo (al menos en un mundo ideal).

Para esto, ademas de aprender lenguajes de programacion, tenemos que aprender a resolver problemas y a pensar de una manera distinta. La computadora hace exactamente lo que le decimos que haga, nada mas y nada menos. Es por esto que es super importante que aprendamos a pensar los problemas de una manera clara, concisa y exacta.

# Desarrollo de programas
Para poder darle instrucciones claras a la computadora vamos a pensar los problemas de la siguiente manera. Aca, de mas esta decir, que todos tenemos nuestra propia forma de pensar y el metodo que le sirve a uno no tiene por que servirle a otro. Yo tengo la intencion de darles una manera simple de hacerlo y que a partir de eso, cada uno pueda, con la practica y la experiencia, desarrollar su propia forma de pensar.

Algo util es pensarlo en terminos de entrada y salida, como si fuera una caja negra. No sabemos como tiene que ser el programa que queremos, pero sabemos que queremos que reciba ciertos datos (entrada) y nos de cierta respuesta (salida). Esto deberia orientar bastante la pregunta de que deberia hacer el programa con los datos que e damos, para que nos de la respuesta que queremos.

Podemos comenzar pensando los pasos a seguir para obtener esa respuesta en un lenguaje coloquial y luego ir formalizandolo hasta llegar a una solucion generalizada en algun lenguaje de programacion.

## Que es un algoritmo
Honestamente esto es medio chamuyo, es la misma definicion que te van a dar en casi cualquier curso relacionado con programas y despues nunca la vas a usar, pero te la doy para no romper con la tradicion.
> _Un algoritmo se define como un metodo que se realiza paso a paso para solucionar un problema. Todo algoritmo termina en un numero finito de pasos._

Lo mas importante de un algoritmo es que debe ser...
- ...**preciso**, es decir, bien definido en cuanto a lo que se debe hacer, sin ambiguedades
- ...**definido**. Esto quiere decir que dada la misma, entrada, deberia producir siempre la misma salida (Esta no es enteramente cierta, pero por ahora digamos que es asi)
- ...**finito**. si se sigue un algoritmo, en algun momento tiene que terminar y darme una respuesta. Si no, que gracia tiene?

No les voy a dar un ejemplo chamuyo de lo que puede ser un algoritmo. Cualquier serie de pasos que sigas para completar una tarea... es un algoritmo.

## Pruebas
Otra parte super importante y ventajosa de la programacion son las pruebas. No estamos trabajando con explosivos, que solo se pueden explotar una vez y despues es costoso reemplazarlos. Tenes una compu que no tiene ningun tipo de problema con correr el programa una y mil veces, aprovechalo,
Un programa no esta terminado hasta que no lo testees. Este tipo de pruebas no solo muestran como funciona tu programa en situaciones reales, sino que suelen ser mucho mas rapidas, eficientes, y divertidas que releer tu codigo 90 veces y preguntarte donde podria llegar a haber un error.
Una vez que encontras un comportamiento extrano te podes poner a buscar que puede causarlo, arrancarte los pelos, pedir ayuda y arrepentirte de haber tocado un lenguaje de programacion alguna vez.

# Como hacer un programa
En este curso vamos a trabajar con Python. Para esto hay que instalar Python, si es que no lo tenes de antes.

## Instalar Python

### Windows
Aca es bastante sencillo. Vamos al sitio de Python. Googlealo... y va a haber un boton enorme para descargar la ultima version. Al dia de hoy, eso deberia ser la 3.10.5, pero cualquiera que empiece con el numero 3 va a servir.

### Mac OS
Para mac podemos hacer lo mismo que en Windows. Aca, puede haber alguno que piense que es mejor instalarlo por `homebrew`. Es verdad que es mil veces mas comodo y que deberias usar `brew` de todos modos, pero hay un problemita en este caso.
El paquete de Python que esta en ese manager de paquetes no instala la dependencia Tcl/Tk... Esto quiere decir que por defecto no vas a poder tener Tkinter (igual deberias usar Qt5, pero bueno). No es el fin del mundo, pero aun asi no esta bueno que tu instalacion no incluya bibliotecas estandar de graficos.

### Linux
Creo que si usas Linux no vas a necesitar mucha ayuda para instalar Python pero depende de tu distro. Aca te dejo un par de opciones a ver si la pego.
#### Arch
```bash
$ sudo pacman -S python
```

#### Ubuntu (apt)
```bash
$ sudo apt install python
```

#### Fedora
```bash
$ sudo dnf install python3
```

## Editor de Texto
Ademas de Python, vamos a necesitar un lugar donde escribir programas en Python. Para esto se puede usar literalmente cualquier programa que permita editar texto, hasta Word... aunque, obviamente, no es recomendable. En general, una buena recomendacion es VSCode, pero cada uno tiene su propio editor de texto favorito.

Para instalarlo valen practicamente todos los mismos pasos que para instalar Python asi que no me voy a gastar en escribir mas y, en el peor de los casos, es algo super googleable como casi todas las cosas que esten en este repo.

La ventaja de usar un editor de texto como Visual Studio Code (VSCode) es que resalta con colores ciertas palabras clave de un programa. Esto por mas tonto que parezca es una ventaja enorme, porque hace a los programas mil veces mas legibles. Tambien tiene otras ventajas como integraciones para correr el codigo en el mismo editor y poder analizar el estado de variables y otras cosas que podemos aprender mas adelante.

Por ahora, si ya instalaste VSCode, andate a la solapa de extensione (los cuadraditos que aparecen sobre la izquerda de la pantalla) y en el buscador pone "Python" e instalate la primera extension que tiene el logo de Python. Ya estas en condiciones de programar en Python.
