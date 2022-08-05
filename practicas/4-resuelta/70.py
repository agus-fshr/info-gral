def main():
    letra = str(input("Ingrese una letra: "))
    if len(letra) != 2:
        print("Eso no es UNA letra")
    else:
        if letra.islower():
            print("Es una minuscula")
        elif letra.isupper():
            print("Es mayuscula")

if __name__ == "__main__":
    main()
