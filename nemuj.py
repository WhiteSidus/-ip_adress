print("Vítejte v programu na převod IP adres")

spusob = input("Zadejte způsob převodu (Dec/Bin): ")
ip_address = input("Zadejte IP adresu: ")

if spusob == "Bin":
    # Rozdělení IP adresy na jednotlivé oktety
    octets = ip_address.split('.')
    binary_ip = ""
    # Převod každého oktetu na binární formát
    for octet in octets:
        decimal_octet = int(octet)
        if 0 <= decimal_octet <= 255:
            binary_octet = bin(decimal_octet)[2:].zfill(8)  # Zabezpečuje, aby každý oktet měl 8 bitů
            binary_ip += binary_octet + '.'
        else:
            print("Neplatný oktet:", octet)
            exit(1)
    binary_ip = binary_ip[:-1]  # Odstranění poslední tečky
    print("Binární IP adresa:", binary_ip)

elif spusob == "Dec":
    # Rozdělení binární IP adresy na jednotlivé oktety
    binary_octets = ip_address.split('.')
    decimal_ip = ""
    # Převod každého binárního oktetu na desítkový formát
    for binary_octet in binary_octets:
        decimal_octet = str(int(binary_octet, 2))
        decimal_ip += decimal_octet + '.'
    decimal_ip = decimal_ip[:-1]  # Odstranění poslední tečky
    print("Desítková IP adresa:", decimal_ip)

else:
    print("zadejte prosím 'Dec' nebo 'Bin'.")