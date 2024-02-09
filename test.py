print ("Vitejte v programu na prevod IP adres")

spusob = input("Zadejte sbusob (Dec/Bin): ")

if spusob == "Dec":
    decimal_ip = input("Zadejte desítkovou IP adresu: ")

    # Rozdělení IP adresy na jednotlivé oktety
    octets = decimal_ip.split('.')

    # Kontrola platnosti oktetů
    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            print("Chybný vstup: Neplatný oktet.")
            exit(1)

    # Klasifikace třídy IP adresy
    first_octet = int(octets[0])
    if 1 <= first_octet <= 126:
        print("IP adress má A class")
    elif 128 <= first_octet <= 191:
        print("IP adress má B class")
    elif 192 <= first_octet <= 223:
        print("IP adresa má třídu C.")
    elif 224 <= first_octet <= 239:
        print("IP adresa má třídu D.")
    elif 240 <= first_octet <= 254:
        print("IP adresa má třídu E.")
    else:
        print("Chyba")

    # Převod na binární číslo
    binary_ip = '.'.join(bin(int(octet))[2:].zfill(8) for octet in octets)
    print("Binární IP adresa:", binary_ip)

elif spusob == "Bin":
    binary = input("Zadejte binární číslo: ")
    # Rozdělení binární IP adresy na jednotlivé oktety
    binary_octets = binary.split('.')
    decimal_ip = ""
    # Převod každého binárního oktetu na desítkový formát
    for binary_octet in binary_octets:
        if binary_octet:  # Kontrola prázdného řetězce
            decimal_octet = str(int(binary_octet, 2))
            decimal_ip += decimal_octet + '.'
        else:
            print("Chybný vstup: prázdný oktet.")
            exit(1)
        
    decimal_ip = decimal_ip[:-1]  # Odstranění poslední tečky
    
    # Klasifikace třídy IP adresy
    first_octet = int(decimal_ip.split('.')[0])
    if 1 <= first_octet <= 126:
        print ("IP adress má A class")
    elif 128 <= first_octet <= 191:
        print ("IP adress má B class")
    elif 192 <= first_octet <= 223:
        print ("IP adress má C class")
    elif 224 <= first_octet <= 239:
        print ("IP adress má D class")
    elif 240 <= first_octet <= 254:
        print ("IP adress má E class")
    else:
        print("Chyba")
    
    print("Desítková IP adresa:", decimal_ip)

else:
    print("Chyba")