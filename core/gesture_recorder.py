import argparse

from infrastructure.filesystem import carregar_gestos, salvar_modelo
from infrastructure.camera import capturar_gestos
from core.gesture_trainer import treinar_modelo

def gravar_gestos():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gesto", type=str, help="Nome do gesto a ser gravado")
    args = parser.parse_args()

    gestos = carregar_gestos()

    if args.gesto:
        if args.gesto in gestos.values():
            gestos = {label: nome for label, nome in gestos.items() if nome == args.gesto}
        else:
            print(f"Gesto '{args.gesto}' não encontrado.")
            exit(1)

    dados, rotulos = capturar_gestos(gestos)
    modelo = treinar_modelo(dados, rotulos)
    salvar_modelo(modelo)
