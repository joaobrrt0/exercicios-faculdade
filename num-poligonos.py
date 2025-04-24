import math


num_lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado (em cm): "))


if num_lados < 3:
    print("NÃO É UM POLÍGONO")

elif num_lados == 3:

    area = (medida_lado ** 2 * math.sqrt(3)) / 4
    print("TRIÂNGULO")
    print(f"Área: {area:.2f} cm²")

elif num_lados == 4:
    # Área do quadrado: lado²
    area = medida_lado ** 2
    print("QUADRADO")
    print(f"Área: {area:.2f} cm²")

elif num_lados == 5:
    print("PENTÁGONO")

else:
    print("POLÍGONO NÃO IDENTIFICADO")
