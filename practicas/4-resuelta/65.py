def main():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    
    if n1**2 == n2:
        print("El segundo es el cuadrado del primero")
    elif n2 < n1**2:
        print("El segundo es menor que el cuadrado del primero")
    else:
        print("El segundo es mayor que el cuadrado del primero")

if __name__ == "__main__":
    main()
