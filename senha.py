# Solicita ao usuário criar uma senha inicial
senha_inicial = input("Crie uma senha inicial: ")

# Imprime mensagem de confirmação
print("Senha criada com sucesso!")

# Solicita ao usuário digitar a senha para verificação
senha_digitada = input("Digite sua senha para acessar: ")

# Verifica se a senha digitada é igual à senha criada
if senha_digitada == senha_inicial:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")
