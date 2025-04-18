# Reconhecimento de Gestos 

Este projeto implementa um sistema de reconhecimento de gestos de mão utilizando Python, OpenCV, MediaPipe e Scikit-learn, com uma estrutura baseada nos princípios da Clean Architecture para garantir uma organização clara e modular do código. Desenvolvido com fins educacionais, ele foi criado como parte do Projeto Aplicado da minha graduação.

## Estrutura do Projeto

```
projeto-aplicado/
│
├── app/                  
│   ├── cli.py
│   ├── main.py
│   └── test.py
│
├── core/                 
│   ├── cli_actions.py
│   ├── gesture_recorder.py
│   ├── gesture_tester.py
│   └── gesture_trainer.py
│
├── domain/               
│   └── models.py
│
├── infrastructure/       
│   ├── camera.py
│   └── filesystem.py
│
├── utils/                
│   ├── gestos.json
│   └── modelo_gestos.pkl
│
├── requirements.txt      
└── README.md             
```

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/whoisdon/HandSign.git
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### 1. Iniciar a interface de linha de comando (CLI)

Execute:
```bash
python -m app.cli
```

Você verá um menu interativo com as opções:
- Criar um Novo Gesto
- Gravar Todos os Gestos
- Gravar um Gesto Específico
- Testar Reconhecimento de Gestos
- Listar Todos os Gestos
- Sair

### 2. Fluxo sugerido

1. **Criar um novo gesto:** Adicione um gesto ao sistema.
2. **Gravar gestos:** Grave exemplos dos gestos usando a webcam.
3. **Testar reconhecimento:** Teste o reconhecimento em tempo real.
4. **Listar gestos:** Veja todos os gestos cadastrados.

### 3. Estrutura dos arquivos de dados

- `utils/gestos.json`: Armazena os gestos cadastrados.
- `utils/modelo_gestos.pkl`: Modelo treinado para reconhecimento.

## Observações

- Certifique-se de que sua webcam está conectada.
- O projeto utiliza MediaPipe para detecção de mãos e Scikit-learn para classificação.
- O sistema é modular e pode ser expandido facilmente para novos gestos.

## Licença

Este projeto é apenas para fins educacionais.
