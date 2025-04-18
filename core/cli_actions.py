import os
import inquirer
from infrastructure.filesystem import carregar_gestos, salvar_gestos

GESTOS_PATH = ".cache/gestos.json"

def criar_novo_gesto():
    resposta = inquirer.prompt([
        inquirer.Text('gesto', message="Digite o nome do novo gesto")
    ])

    nome_gesto = resposta['gesto']
    gestos = carregar_gestos()

    if nome_gesto in gestos.values():
        print(f"O gesto '{nome_gesto}' já existe!")
        return

    novo_label = max([int(k) for k in gestos.keys()], default=-1) + 1
    gestos[str(novo_label)] = nome_gesto
    salvar_gestos(gestos)
    os.system(f"python -m app.main --gesto {nome_gesto}")

def gravar_gesto():
    os.system("python -m app.main")

def testar_gestos():
    os.system("python -m app.test")

def gravar_gesto_especifico():
    gestos = carregar_gestos()
    if not gestos:
        print("Nenhum gesto salvo.")
        return

    lista_gestos = [f"{label}: {nome}" for label, nome in gestos.items()]
    resposta = inquirer.prompt([
        inquirer.List("gesto_escolhido", message="Escolha um gesto para gravar:", choices=lista_gestos)
    ])

    _, nome_gesto = resposta["gesto_escolhido"].split(": ", 1)
    os.system(f"python -m app.main --gesto {nome_gesto}")

def listar_gestos():
    gestos = carregar_gestos()
    if not gestos:
        print("Nenhum gesto salvo.")
        return

    lista_gestos = [f"{label}: {nome}" for label, nome in gestos.items()]
    inquirer.prompt([
        inquirer.List("gestos", message="Gestos salvos", choices=lista_gestos)
    ])
