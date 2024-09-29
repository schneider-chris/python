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
print("Seja bem vindo," + nome)

while True:
    menu()
    user = int(input("Digite o número da opção desejada:"))

    #primeira escolha do menu principal
    if user == 1:
        pizza_salgada()
        escolha = int(input("Opção desejada:"))

        #primeira pizza salgada
        if escolha == 1:
            print("Você escolheu a pizza de Mussarela.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #segunda pizza salgada
        if escolha == 2:
            print("Você escolheu a pizza de Calabresa.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #terceira pizza salgada
        if escolha == 3:
            print("Você escolheu a pizza de Frango com Catupiry.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #quarta pizza salgada
        if escolha == 4:
            print("Você escolheu a pizza de Strogonoff de Carne.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

    #segunda escolha do menu principal
    elif user == 2:
        pizza_doce()
        escolha = int(input("Opção desejada:"))

        #primeira pizza doce
        if escolha == 1:
            print("Você escolheu a pizza de Brigadeiro.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #segunda pizza doce
        if escolha == 2:
            print("Você escolheu a pizza de Sensação.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #terceira pizza doce
        if escolha == 3:
            print("Você escolheu a pizza de Prestígio.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #quarta pizza doce
        if escolha == 4:
            print("Você escolheu a pizza de Romeu e Julieta.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!") 
    
    #terceira escolha do menu principal
    elif user == 3:
        lanches()
        escolha = int(input("Opção desejada:"))

        #primeiro lanche
        if escolha == 1:
            print("Você escolheu o lanche X-frango.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #segundo lanche
        if escolha == 2:
            print("Você escolheu o lanche X-bacon.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #terceiro lanche
        if escolha == 3:
            print("Você escolheu o lanche X-salada.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #quarto lanche
        if escolha == 4:
            print("Você escolheu o lanche X-egg.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

    #quarta escolha do menu principal
    elif user == 4:
        bebidas()
        escolha = int(input("Opção desejada:"))

        #primeira bebida
        if escolha == 1:
            print("Você escolheu Coca-Cola.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #segunda bebida
        if escolha == 2:
            print("Você escolheu Guaraná.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #terceira bebida
        if escolha == 3:
            print("Você escolheu Fanta.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

        #quarta bebida
        if escolha == 4:
            print("Você escolheu Água.")
            finalizar()
            opção = int(input("O que você deseja?"))
            
            if opção == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opção == 2:
                continue
            else:
                print("Opção inválida!")

    
    #outra opção 
    else:
        print("Opção inválida. Tente novamente!")