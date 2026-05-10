#Menu principal
import menu

while True:
    menu.Menu()
    
    try:
        opcao = int(input("Digite uma opção: "))
        
        if opcao == 1:
            print("   Cadastrar drones   \n")
        elif opcao == 2:
            print("  Listar drones  \n")
        elif opcao == 3:
            print("  Monitorar status")
        elif opcao == 4:
            print("  Controlar missão  \n")
        elif opcao == 5:
            print("  Câmera  \n")
        elif opcao == 6:
            print("  Histórico  ")
        elif opcao == 0:
            print("  Encerra o programa  ")
            break
        else:
            print("OPÇÃO INVÁLIDA")
    except ValueError:
        print("Digite apenas números")
    
        