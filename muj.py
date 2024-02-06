print ("Vitejte v programu na prevod IP adres")

spusob = input("Zadejte sbusob (Dec/Bin): ")

if spusob == "Bin":
    binary = input("Zadejte binární číslo: ")
    #Převod na desitkové číslo
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
        if 1 <= decimal <= 126:
            print ("IP adress má A class")
        elif 128 <= decimal <= 191:
            print ("IP adress má B class")
        elif 192 <= decimal <= 223:
            print ("IP adress má C class")
        elif 224 <= decimal <= 239:
            print ("IP adress má D class")
        elif 240 <= decimal <= 254:
            print ("IP adress má E class")
        else:
            print("Chyba")
    print(decimal)

elif spusob == "Dec":
    decimal = int(input("Zadejte desítkové číslo: "))
    #Převod na binární číslo
    binary = bin(decimal)[2:]
    print(binary)
else:
    print("Chyba")