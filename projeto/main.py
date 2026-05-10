from menu import Menu
from funcoes import cadastrar, listar, buscar


# main.py
from menu import Menu
from funcoes import cadastrar, listar, buscar

while True:
    Menu()

    try:
        opcao = int(input("Digite a sua opção: "))

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            buscar()
        elif opcao == 0:
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Escolha entre 0 e 3.")

    except ValueError:
        print("Erro! Digite apenas números no menu.")