#registrar e exibir histórico de voos
import drones

def ver_historico():
    busca_id = int(input("Digite o ID do drone: "))
    
    sintuacao = None
    
    for historico_drone in drones.lista:
        if historico_drone['id'] == busca_id:
            sintuacao = historico_drone
            break
        
        
    if sintuacao == None:
        print("Drone não encontrado")
    elif len(sintuacao['historico']) == 0:
        print("Nâo há nada no histórico")
    else:
        
        print(f"Histórico do drone {sintuacao['nome']}:")
        for i, historico_completo in enumerate(sintuacao['historico']):
            print(f"{i+1} - {historico_completo}")