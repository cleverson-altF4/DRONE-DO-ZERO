#Cadastrar e listar drones
import drones

def cadastrar_drones():
    dicionario = {}
    dicionario['id'] = len(drones.lista) + 1
    dicionario['nome'] = str(input("Digite o nome do drone: ")).strip()
    dicionario['modelo'] = str(input("Digite o modelo do drone: ")).strip()
    dicionario['bateria'] = 100
    dicionario['altitude'] = 0
    dicionario['status'] = 'solo'
    dicionario['camera'] = False
    dicionario['historico'] = [] # Lista vazia
    drones.lista.append(dicionario)
    print(f"Drone: {dicionario['nome']} cadastrado!  |  ID: {dicionario['id']}")
    
    
def listar():
    if len(drones.lista) == 0:
        print("A lista está vazia")
    else:
        for drone in drones.lista:
            print(f"ID: {drone['id']}")
            print(f"Nome: {drone['nome']}")
            print(f"Modelo: {drone['modelo']}")
            print(f"Bateria: {drone['bateria']}%")
            print(f"Status: {drone['status']}")
            print(f"Câmera: {drone['camera']}")
            
            if len(drone['historico']) == 0:
                print("Nenhum evento registrado")
            else:
                for evento in drone['historico']:
                    print(f" - {evento}")
            
            