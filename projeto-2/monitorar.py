#Ver bateria, altitude e status
import drones

def monitorar():
    
    busca_monitoramento = int(input("Digite o Id do monitoramento: "))
    
    drone_encontrado = None
    
    for lista_drones in drones.lista:
        
        if lista_drones['id'] == busca_monitoramento:
            drone_encontrado = lista_drones
            break
    
    if drone_encontrado == None:
        print("Não foi encontrado nenhum drone na lista")
    else:
        print(f"Nome {drone_encontrado['nome']}")
        print(f"Modelo {drone_encontrado['modelo']}")
        print(f"Bateria: {drone_encontrado['bateria']}%")

        if drone_encontrado['bateria'] < 20:
            print("Alerta: Bateria fraca!")      
        
        print(f"Altitude: {drone_encontrado['altitude']}M")
        print(f"Status: {drone_encontrado['status']}")
        if drone_encontrado['camera'] == True:
            print("Câmera: Ligada")
        else:
            print("Câmera: Desligada")

    
    