
# desafio_10.py
def calcular_area(largura, altura):
    area = largura * altura
    return area

# Usando a função
l = float(input("Largura do terreno: "))
a = float(input("Comprimento do terreno: "))

resultado = calcular_area(l, a)
print(f"A área total do terreno é de {resultado}m².")
