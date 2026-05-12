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
    
            
def patrulhar():
    id_buscador_patrulha = int(input("Digite o ID do drone: "))
    drone_encontrado = None
    
    for drone_patrulha in drones.lista:
        if drone_patrulha['id'] == id_buscador_patrulha:
            drone_encontrado = drone_patrulha
            break
        
    
    if drone_encontrado == None:
        print("Drone não encontrado")
    elif drone_encontrado['status'] != 'voando':
        print("O drone precisa está voando primeiro")
    else:
        drone_encontrado['status'] = 'patrulhando'
        
        while True:
            area = input("Digite a área da patrulha: ").strip()
            if area.isnumeric():
                print("Não é permitido números")
            else:
                break
        
        
        drone_encontrado['historico'].append(f"Patrulhando {area}")
        
        print(f"Drone {drone_encontrado['nome']} patrulhando área {area}")