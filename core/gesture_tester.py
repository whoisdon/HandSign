from infrastructure.filesystem import carregar_modelo, carregar_gestos
from infrastructure.camera import capturar_predicoes

def testar_gestos():
    modelo = carregar_modelo()
    gestos = carregar_gestos()

    gestos_map = {int(k): v for k, v in gestos.items()}

    capturar_predicoes(modelo, gestos_map)