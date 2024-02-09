print ("Vitejte v programu na prevod IP adres")

spusob = input("Zadejte sbusob (Dec/Bin): ")

if spusob == "Bin" or "bin":
    binary = input("Zadejte binární číslo: ")
    # Rozdělení binární IP adresy na jednotlivé oktety
    binary_octets = binary.split('.')
    decimal_ip = ""
    # Převod každého binárního oktetu na desítkový formát
    for binary_octet in binary_octets:
        decimal_octet = str(int(binary_octet, 2))
        decimal_ip += decimal_octet + '.'
    decimal_ip = decimal_ip[:-1]  # Odstranění poslední tečky

    # Určujeme class IP adresy
    for digit in decimal_ip:
        if 1 <= decimal_ip <= 126:
            print ("IP adress má A class")
        elif 128 <= decimal_ip <= 191:
            print ("IP adress má B class")
        elif 192 <= decimal_ip <= 223:
            print ("IP adress má C class")
        elif 224 <= decimal_ip <= 239:
            print ("IP adress má D class")
        elif 240 <= decimal_ip <= 254:
            print ("IP adress má E class")
        else:
            print("Chyba")
    print("Desítková IP adresa:", decimal_ip)


elif spusob == "Dec":
    decimal = int(input("Zadejte desítkové číslo: "))

    #Převod na binární číslo
    binary = bin(decimal)[2:]
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
    print(binary)
else:
    print("Chyba")