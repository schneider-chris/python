def menu():
    print("Essas são as opções do nosso cardápio:")
    print("1- Pizzas Salgadas")
    print("2- Pizzas Doces")
    print("3- Lanches")
    print("4- Bebidas")

def pizza_salgada():
    print("Temos os seguintes sabores:")
    print("1- Mussarela")
    print("2- Calabresa")
    print("3- Frango com Catupiry")
    print("4- Strogonoff de Carne")






print("Olá!")
nome = input("Digite seu nome aqui:")
print("Bem vindo," + nome)


menu()

user = int(input("Digite o número da opção desejada:"))


if user == 1:
    pizza_salgada()
