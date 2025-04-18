import os
import inquirer
from infrastructure.filesystem import carregar_gestos

GESTOS_PATH = ".cache/gestos.json"

questions = [
    inquirer.List(
        "opcao",
        message="Escolha uma opção",
        choices=[
            "Criar um Novo Gesto",
            "Gravar Todos os Gestos",
            "Gravar um Gesto Específico",
            "Testar Reconhecimento de Gestos",
            "Listar Todos os Gestos",
            "Sair"
        ],
    )
]

while True:
    from core.cli_actions import (
        criar_novo_gesto, gravar_gesto, gravar_gesto_especifico,
        testar_gestos, listar_gestos
    )


    answers = inquirer.prompt(questions)
    opcao = answers["opcao"]

    if opcao == "Criar um Novo Gesto":
        criar_novo_gesto()
    elif opcao == "Gravar Todos os Gestos":
        gravar_gesto()
    elif opcao == "Gravar um Gesto Específico":
        gravar_gesto_especifico()
    elif opcao == "Testar Reconhecimento de Gestos":
        testar_gestos()
    elif opcao == "Listar Todos os Gestos":
        listar_gestos()
    elif opcao == "Sair":
        break