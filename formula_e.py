import json
import pandas as pd
import random

# Função para carregar dados do arquivo JSON com codificação utf-8
def carregar_dados(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    return dados

# Função para salvar informações do usuário em um arquivo JSON
def salvar_usuario(nome, idade, nome_acesso):
    usuario = {
        "nome": nome,
        "idade": idade,
        "nome_acesso": nome_acesso
    }
    
    try:
        with open('usuarios.json', 'r', encoding='utf-8') as f:
            usuarios_existentes = json.load(f)
    except FileNotFoundError:
        usuarios_existentes = []
    
    usuarios_existentes.append(usuario)
    
    with open('usuarios.json', 'w', encoding='utf-8') as f:
        json.dump(usuarios_existentes, f, ensure_ascii=False, indent=4)

# Função para salvar informações da corrida em um arquivo JSON
def salvar_corrida(resultados):
    try:
        with open('corridas.json', 'r', encoding='utf-8') as f:
            corridas_existentes = json.load(f)
    except FileNotFoundError:
        corridas_existentes = []
    
    corridas_existentes.append(resultados)
    
    with open('corridas.json', 'w', encoding='utf-8') as f:
        json.dump(corridas_existentes, f, ensure_ascii=False, indent=4)

# Função de login
def tela_login():
    print("Bem-vindo ao sistema!")
    
    nome = input("Informe seu nome: ")
    
    while True:
        idade = input("Informe sua idade: ")
        if idade.isdigit() and int(idade) >= 18:
            idade = int(idade)
            break
        else:
            print("Idade inválida. Você deve ter pelo menos 18 anos.")

    nome_acesso = input("Informe seu nome de acesso: ")
    
    salvar_usuario(nome, idade, nome_acesso)
    
    print(f"\nLogin realizado com sucesso! Bem-vindo, {nome}.\n")
    return nome, idade, nome_acesso

# Funções para exibir dados
def exibir_pilotos(dados_pilotos):
    pilotos = pd.DataFrame(dados_pilotos["pilotos"])
    print("\n--- Pilotos ---")
    print(pilotos)

def exibir_carros(dados_carros):
    carros = pd.DataFrame(dados_carros["carros"])
    print("\n--- Carros ---")
    print(carros)

def exibir_equipes(dados_equipes):
    equipes = pd.DataFrame(dados_equipes["equipes"])
    print("\n--- Equipes ---")
    print(equipes)

def exibir_pistas(dados_pistas):
    pistas = pd.DataFrame(dados_pistas["pistas"])
    print("\n--- Pistas ---")
    print(pistas)

# Função para corrida
def pista_de_corrida():
    while True:
        num_corredores = input("Quantas pessoas vão correr? ")
        if num_corredores.isdigit() and int(num_corredores) > 0:
            num_corredores = int(num_corredores)
            break
        else:
            print("Por favor, insira um número válido.")

    corredores = []
    for i in range(num_corredores):
        nome_corredor = input(f"Informe o nome do corredor {i + 1}: ")
        corredores.append(nome_corredor)

    # Simulação da corrida
    vencedor = random.choice(corredores)
    
    resultados = {
        "corredores": corredores,
        "vencedor": vencedor
    }

    salvar_corrida(resultados)
    
    print(f"\n--- Resultados da Corrida ---")
    print(f"Corredores: {', '.join(corredores)}")
    print(f"Vencedor: {vencedor}")

    # Opção de revanche
    while True:
        revanche = input("\nVocê gostaria de fazer uma revanche? (s/n): ").strip().lower()
        if revanche == 's':
            print("Reiniciando a corrida...")
            pista_de_corrida()
            break
        elif revanche == 'n':
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida! Responda com 's' ou 'n'.")

# Função do menu para interagir com o usuário
def menu(dados_pilotos, dados_carros, dados_equipes, dados_pistas):
    while True:
        print("\n*** MENU ***")
        print("1. Pilotos")
        print("2. Carros")
        print("3. Equipes")
        print("4. Pistas")
        print("5. Vamos correr?")
        print("6. Encerrar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_pilotos(dados_pilotos)
        elif opcao == '2':
            exibir_carros(dados_carros)
        elif opcao == '3':
            exibir_equipes(dados_equipes)
        elif opcao == '4':
            exibir_pistas(dados_pistas)
        elif opcao == '5':
            pista_de_corrida()
        elif opcao == '6':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Carregar os dados dos arquivos JSON
dados_pilotos = carregar_dados('dados_pilotos.json')
dados_carros = carregar_dados('dados_carros.json')
dados_equipes = carregar_dados('dados_equipes.json')
dados_pistas = carregar_dados('dados_pistas.json')

# Executar a tela de login
tela_login()

# Executar o menu com os dados carregados
menu(dados_pilotos, dados_carros, dados_equipes, dados_pistas)
