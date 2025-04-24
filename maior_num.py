# Entrada dos dados
a = int(input("Digite o primeiro valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))
c = int(input("Digite o terceiro valor inteiro: "))

# Verificação do maior valor
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

# Saída
print(f"O maior valor é: {maior}")
