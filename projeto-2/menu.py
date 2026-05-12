#Funções que recebe o menu

def menu():
    print("|","-"*10," Menu ","-"*15,"|")
    print('''
          
          \033[33m[1]\033[0m - Cadastrar drone
          \033[33m[2]\033[0m - Listar drones
          \033[33m[3]\033[0m - Monitorar status
          \033[33m[4]\033[0m - Controlar missão
          \033[33m[5]\033[0m - Câmera
          \033[33m[6]\033[0m - Histórico
          \033[33m[0]\033[0m - Encerra processo - ''')
    print()