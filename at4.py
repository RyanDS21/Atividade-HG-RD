login = "admin"
senha = "123"

vf1 = input("Digite o Login: ")
vf2 = str(input("Digite a Senha: "))

if vf1 == login and vf2 == senha:
    print("Olá admin, Seja bem-vindo !")
else:
    print("Login ou Senha incorretos, tente novamente")