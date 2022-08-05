# 500, 200, 100, 50, 20, 10, 5, 2, 1

def main():
    n = int(input("Numero: "))
    resto = n % 500
    print(f"{n//500} billetes de 500")
    print(f"{resto//200} biletes de 200")
    resto%=200
    print(f"{resto//100} billetes de 100")
    resto%=100
    print(f"{resto//50} billetes de 50")
    resto%=50
    print(f"{resto//20} billetes de 20")
    resto%=20
    print(f"{resto//10} billetes de 10")
    resto%=10
    print(f"{resto//5} billetes de 5")
    resto%=5
    print(f"{resto//2} monedas de 2")
    resto%=2
    print(f"{resto//2} moneda de 1")

if __name__ == "__main__":
    main()

# Deberiamos revisitar este problema cuando sepamos un poco mas de Python ;)
