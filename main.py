#funções
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

def pizza_doce():
    print("Temos os seguintes sabores:")
    print("1- Brigadeiro")
    print("2- Sensação")
    print("3- Prestígio")
    print("4- Romeu e Julieta")

def lanches():
    print("Temos as seguintes opções de lanches:")
    print("1- X-frango")
    print("2- X-bacon")
    print("3- X-salada")
    print("4- X-egg")

def bebidas():
    print("Temos as seguintes opções de bebidas:")
    print("1- Coca-Cola")
    print("2- Guaraná")
    print("3- Fanta")
    print("4- Água")

def finalizar():
    print("Ok, deseja finalizar o pedido ou voltar ao menu?")
    print("1- Finalizar pedido")
    print("2- Voltar ao menu")


#apresentação
print("Olá!")
nome = input("Digite seu nome aqui:")
print("Seja bem vindo," + nome )
print()

while True:
    menu()
    print()
    user = int(input("Digite o número da opção desejada:"))

    #primeira escolha do menu principal
    if user == 1:
        print()
        pizza_salgada()
        print()
        escolha = int(input("Opção desejada:"))

        #primeira pizza salgada
        if escolha == 1:
            print()
            print("Você escolheu a pizza de Mussarela.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #segunda pizza salgada
        if escolha == 2:
            print()
            print("Você escolheu a pizza de Calabresa.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #terceira pizza salgada
        if escolha == 3:
            print()
            print("Você escolheu a pizza de Frango com Catupiry.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #quarta pizza salgada
        if escolha == 4:
            print()
            print("Você escolheu a pizza de Strogonoff de Carne.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

    #segunda escolha do menu principal
    elif user == 2:
        print()
        pizza_doce()
        print()
        escolha = int(input("Opção desejada:"))

        #primeira pizza doce
        if escolha == 1:
            print()
            print("Você escolheu a pizza de Brigadeiro.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #segunda pizza doce
        if escolha == 2:
            print()
            print("Você escolheu a pizza de Sensação.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #terceira pizza doce
        if escolha == 3:
            print()
            print("Você escolheu a pizza de Prestígio.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #quarta pizza doce
        if escolha == 4:
            print()
            print("Você escolheu a pizza de Romeu e Julieta.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n") 
    
    #terceira escolha do menu principal
    elif user == 3:
        print()
        lanches()
        print()
        escolha = int(input("Opção desejada:"))

        #primeiro lanche
        if escolha == 1:
            print()
            print("Você escolheu o lanche X-frango.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?\n"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #segundo lanche
        if escolha == 2:
            print()
            print("Você escolheu o lanche X-bacon.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #terceiro lanche
        if escolha == 3:
            print()
            print("Você escolheu o lanche X-salada.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!\n")

        #quarto lanche
        if escolha == 4:
            print()
            print("Você escolheu o lanche X-egg.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

    #quarta escolha do menu principal
    elif user == 4:
        print()
        bebidas()
        print()
        escolha = int(input("Opção desejada:"))

        #primeira bebida
        if escolha == 1:
            print()
            print("Você escolheu Coca-Cola.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #segunda bebida
        if escolha == 2:
            print()
            print("Você escolheu Guaraná.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #terceira bebida
        if escolha == 3:
            print()
            print("Você escolheu Fanta.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

        #quarta bebida
        if escolha == 4:
            print()
            print("Você escolheu Água.\n")
            finalizar()
            print()
            opção = int(input("O que você deseja"))
            
            if opção == 1:
                print()
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                print()
                continue
            else:
                print()
                print("Opção inválida!\n")

    #outra opção 
    else:
        print("Opção inválida. Tente novamente!")