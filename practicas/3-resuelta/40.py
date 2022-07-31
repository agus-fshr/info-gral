def main():
    euros = float(input("Ctd en euros: "))
    tasa = float(input("Tasa de interes (en %): "))
    anos = float(input("Duracion del pzo. fijo (en anos): "))

    print(f"${euros*(1+tasa/100)**anos}")

if __name__ == "__main__":
    main()
