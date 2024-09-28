
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
print("Bem vindo," + nome)

while True: 
    menu()
    user = int(input("Digite o número da opção desejada:"))

#primeira escolha do menu
    if user == 1:
        pizza_salgada()
        escolha = int(input("Número da opção desejada: "))

        #escolha da primeira pizza
        if escolha == 1:
                print("Você escolheu a pizza de Mussarela.")
                finalizar()
                opcao = int(input("Digite sua escolha: "))
                if opcao == 1:
                    print("Pedido finalizado! Obrigado.")
                    break
                elif opcao == 2:
                    continue
                else:
                    print("Opção inválida!")

            #escolha da segunda pizza 
        elif escolha == 2:
                print("Você escolheu a pizza de Calabresa.")
                finalizar()
                opcao = int(input("Digite sua escolha: "))
                if opcao == 1:
                    print("Pedido finalizado! Obrigado.")
                    break
                elif opcao == 2:
                    continue
                else:
                    print("Opção inválida!")

            #escolha da terceira pizza 
        elif escolha == 3:
            print("Você escolheu a pizza de Frango com Catupiry.")
            finalizar()
            opcao = int(input("Digite sua escolha: "))
            if opcao == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opcao == 2:
                continue
            else:
                print("Opção inválida!")

            #escolha da quarta pizza 
        elif escolha == 4:
            print("Você escolheu a pizza de Strogonoff de Carne.")
            finalizar()
            opcao = int(input("Digite sua escolha: "))
            if opcao == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opcao == 2:
                continue
            else:
                print("Opção inválida!")
                    
            #opção errada
        else:
                print("Opção inválida, escolha novamente.")


    elif user == 2:
        pizza_doce()
        escolha = int(input("Número da opção desejada: "))
        if escolha == 1: 2; 3; 4:
        finalizar()
        opcao = int(input("Digite sua escolha: "))
        if opcao == 1:
                print("Pedido finalizado! Obrigado.")
                break
        elif opcao == 2:
            menu()
        else:
            print("Opção inválida")
            finalizar()

    elif user == 3:
        lanches()
        escolha = int(input("Número da opção desejada: "))
        if escolha == 1; 2; 3; 4:
            finalizar()
            opcao = int(input("Digite sua escolha: "))
            if opcao == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opcao == 2:
                menu()
            else:
                print("Opção inválida!")
                finalizar()

    elif user == 4:
        bebidas()
        escolha = int(input("Número da opção desejada: "))
        if escolha == 1; 2; 3; 4:
            finalizar()
            opcao = int(input("Digite sua escolha: "))
            if opcao == 1:
                print("Pedido finalizado! Obrigado.")
                break
            elif opcao == 2:
                menu()
            else:
                print("Opção inválida!")
                finalizar()

    else:
        print("Opção inválida, volte ao menu.")





    

    

