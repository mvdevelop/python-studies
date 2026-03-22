
import random
import time

while True:
    temperatura = random.randint(20, 40)

    print(f"Temperatura: {temperatura}°C")

    if temperatura > 30:
        print("Ventoinha LIGADA")
    else:
        print("Ventoinha DESLIGADA")

    print("-" * 30)

    time.sleep(2)
