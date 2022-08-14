# Informatica General (71.20)
---

## Aclaraciones
### 1. `__name__ == "__main__"`
Muchos archivos `.py` de resoluciones estan estructurados de a siguiente manera:
```Python
def main():
	CODIGO
if __name__ == "__main__":
	main()
```

Esta escrito de esa manera para que el programa solamente corra, si es el archivo principal. No es necesario incluirlo para programas de un solo archivo pero lo hago de todos modos como buena practica para indicar que un archivo esta hecho con intencion de ser ejecutado.

### 2. fstrings
En muchas resoluciones se usan fstrings. Si no saben lo que son o no recuerdan como se usan, son las que tienen la forma `print(f"texto {expresion} texto")`. Estas fstrings o _formatted string literals_ son usadas con regularidad por la comodidad que ofrecen.
