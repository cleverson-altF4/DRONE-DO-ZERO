#Ligar/ desligar camera e tirar foto
import drones

def ligar_camera():
    buscar_camera = int(input("Buscar ID da câmera: "))
    
    drone_encontrado = None
    
    for camera_on in drones.lista:
        if camera_on['id'] == buscar_camera:
            drone_encontrado = camera_on
            break
        
        
    if drone_encontrado == None:
        print("Não foi encontrado o drone")
    elif drone_encontrado['status'] == 'solo':
        print("Nâo pode ligar a câmera")
    elif drone_encontrado['camera'] == True:
        print("A cãmera está ligada")
    else:
        drone_encontrado['camera'] = True
        drone_encontrado['historico'].append('Câmera ligada')
        print(f"Câmera do drone {drone_encontrado['nome']} ligada!")
           
           
def desligar_camera():
    buscar_camera = int(input("Digite o ID da câmera: "))
    
    sintuacao_camera = None
    
    for camera_off in drones.lista:
        if camera_off['id'] == buscar_camera:
            sintuacao_camera = camera_off
            break
        
        
    if sintuacao_camera == None:
        print("Nâo foi encontrado o drone")
    elif sintuacao_camera['camera'] == False:
        print("A câmera já está desligada")
    else:
        sintuacao_camera['camera'] = False
        sintuacao_camera['historico'].append('câmera desligada')
        print(f"Câmera do drone {sintuacao_camera['nome']} Desligada!")
    
    
def tirar_foto():
    busca_id = int(input("Digite o ID do drone: "))
    
    sintuacao_foto = None
    
    for foto in drones.lista:
        if foto['id'] == busca_id:
            sintuacao_foto = foto
            break
        
        
    if sintuacao_foto == None:
        print("Não há câmera")
    elif sintuacao_foto['camera'] == False:
        print("A câmera não pode fotografar")
    else:
        sintuacao_foto['historico'].append("Foto tirada")
        print(f"Foto tirada pelo drone {sintuacao_foto['nome']}")
        