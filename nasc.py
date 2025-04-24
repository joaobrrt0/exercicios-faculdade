
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

from datetime import date
ano_atual = date.today().year


idade = ano_atual - ano_nascimento


if idade >= 16:
    print("Você PODE votar este ano.")
else:
    print("Você NÃO pode votar este ano.")
