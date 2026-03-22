
estado_led = False

while True:
    comando = input("Pressione ENTER para alternar o LED (ou 'sair'): ")

    if comando == "sair":
        break

    estado_led = not estado_led

    if estado_led:
        print("LED LIGADO")
    else:
        print("LED DESLIGADO")
