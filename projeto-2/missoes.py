#Decola, pousar e patrulhar
import drones

def decolar():
    id_buscador_decolar = int(input("Digite o ID do drone: "))
    drone_encontrado = None
    
    for drone in drones.lista:
        if drone['id'] == id_buscador_decolar:
            drone_encontrado = drone
            break
        
    if drone_encontrado == None:
        print("Drone não foi encontrado")
    elif drone_encontrado['bateria'] < 20:
        print("Bateria fraca, não pode decolar")
    elif drone_encontrado['status'] == 'voando':
        print("Drone já está no ar!")
    else:
        drone_encontrado['status'] = 'voando'
        drone_encontrado['altitude'] = 50
        drone_encontrado['historico'].append('decolou')
        print(f"Drone {drone_encontrado['nome']} decolou!")
        
        
        
def pousar():
    id_buscador_pousar = int(input("Digite o ID do drone: "))
    drone_encontrado = None
    for drone_pousado in drones.lista:
        if drone_pousado['id'] == id_buscador_pousar:
            drone_encontrado = drone_pousado
            break
        
    if drone_encontrado == None:
        print("Drone não foi encontrado")
        
    elif drone_encontrado['status'] == 'solo':
        print("Drone já está no chão!")
    else:
        drone_encontrado['status'] = 'solo'
        drone_encontrado['altitude'] = 0
        drone_encontrado['camera'] = False #Desliga a câmera
        drone_encontrado['historico'].append('pousou')
        print(f"Drone {drone_encontrado['nome']} pousou com sucesso!")
    
            