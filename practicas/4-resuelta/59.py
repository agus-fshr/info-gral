def main():
    edad1 = int(input("Edad 1: "))
    edad2 = int(input("Edad 2: "))
    if edad1 > edad2:
        print(f"{edad1} es mayor")
    elif edad1 < edad2:
        print(f"{edad2} es mayor")
    else:
        print("iguales")

    # Una forma branchless
    # return edad1*(edad1>=edad2)+edad2*(edad1<edad2)

if __name__ == "__main__":
    main()
