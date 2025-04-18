import json
import pickle
import os
import inquirer

GESTOS_PATH = "utils/gestos.json"
MODELO_PATH = "utils/modelo_gestos.pkl"

def carregar_gestos():
    with open(GESTOS_PATH, "r") as f:
        return json.load(f)

def salvar_gestos(gestos):
    with open(GESTOS_PATH, "w") as f:
        json.dump(gestos, f, indent=4)

def salvar_modelo(modelo):
    with open(MODELO_PATH, "wb") as f:
        pickle.dump(modelo, f)

def carregar_modelo():
    if not os.path.exists(MODELO_PATH) or os.path.getsize(MODELO_PATH) == 0:
        raise inquirer.prompt([
            inquirer.Confirm(
                "alerta",
                message="O arquivo modelo_gestos.pkl está vazio ou não existe. Não é possível carregar o modelo. \n",
                default=True
            )
        ])
    with open(MODELO_PATH, "rb") as f:
        return pickle.load(f)