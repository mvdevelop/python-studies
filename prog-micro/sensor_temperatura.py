
import random
import time

while True:
    temperatura = random.randint(20, 40)

    print(f"Temperatura: {temperatura}°C")

    if temperatura > 30:
        print("ALERTA: Temperatura alta!")
    
    time.sleep(2)
