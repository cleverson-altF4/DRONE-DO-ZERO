#Menu principal
import menu
from cadastro import cadastrar_drones, listar
from missoes import decolar, pousar, patrulhar
from monitorar import monitorar
from camera import ligar_camera, desligar_camera, tirar_foto
from historico import ver_historico

while True:
    menu.menu()
    
    try:
        opcao = int(input("Digite uma opção: "))
        
        if opcao == 1:
            print("   Cadastrar drones   \n")
            cadastrar_drones()
        elif opcao == 2:
            print("  Listar drones  \n")
            listar()
        elif opcao == 3:
            print("  Monitorar status")
            monitorar()
        elif opcao == 4:
            print("  Controlar missão  \n")
            print('''
                  [1] = Decolar
                  [2] = Pousar
                  [3] = Patrulhar''')
            
            escolha = int(input("Digite uma opção: "))
            if escolha == 1:
                decolar()
            elif escolha == 2:
                pousar()
            elif escolha == 3:
                patrulhar()
            else:
                print("Opção inválida")
            
        elif opcao == 5:
            print("  Câmera  \n")
            
            print('''
                  [1] - Desligar câmera
                  [2] - Ligar câmera
                  [3] - Tirar foto''')
                
            escolha_opcao = int(input("Deseja qual opção da câmera: "))
            if escolha_opcao == 1:
                desligar_camera()
            elif escolha_opcao == 2:
                ligar_camera()
            elif escolha_opcao == 3:
                tirar_foto()
            else:
                print("Opção inválida")
                
        elif opcao == 6:
            print("  Histórico  ")
            ver_historico()
            
        elif opcao == 0:
            print("  Encerra o programa  ")
            break
        else:
            print("OPÇÃO INVÁLIDA")
    except ValueError:
        print("Digite apenas números")
    
        