# funcoes.py
import menu # importa o módulo para acessar a lista

def cadastrar():
    dicionario = {}

    dicionario["nome"] = input("Digite o seu nome: ").strip()

    while True:
        try:
            dicionario["idade"] = int(input("Digite a sua idade: "))
            break  # sai do loop se conseguiu converter
        except ValueError:
            print("Idade inválida! Digite apenas números.")

    while True:
        email = input("Digite o seu email: ").strip()
        if "@" not in email or "." not in email:
            print("Email inválido! Tente novamente.")
        else:
            dicionario["email"] = email
            break

    menu.cadastro.append(dicionario)  # acessa a lista do módulo
    print("Cadastro realizado com sucesso!")


def listar():
    if len(menu.cadastro) == 0:
        print("Não há cadastros.")
    else:
        print("\n===== LISTA DE CADASTROS =====")
        for i, pessoa in enumerate(menu.cadastro, start=1):
            print(f"\n--- Pessoa {i} ---")
            print(f'Nome:  {pessoa["nome"]}')
            print(f'Idade: {pessoa["idade"]}')
            print(f'Email: {pessoa["email"]}')


def buscar():
    busca = input("Deseja buscar qual usuário? ").strip()
    encontrado = False

    for pessoa in menu.cadastro:
        if busca.lower() in pessoa["nome"].lower():
            print(f'\nNome:  {pessoa["nome"]}')
            print(f'Idade: {pessoa["idade"]}')
            print(f'Email: {pessoa["email"]}')
            encontrado = True

    if not encontrado:
        print("Nenhum usuário encontrado com esse nome.")