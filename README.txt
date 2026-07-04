# Instalação e Execução do Projeto

## Requisitos
- Python 3.10 ou superior   (verifique: python3 --version)
- pip
- ngrok (apenas para o canal WhatsApp): https://ngrok.com/download
- Conta gratuita no Twilio (apenas para o canal WhatsApp)
- Token de bot do Telegram (gratuito, via @BotFather)

## Instalação

- Entre na pasta do projeto:
        cd udesc-bot

- Recomendado o uso de um ambiente virtual:
        python3 -m venv venv
        # Linux/Mac:
        source venv/bin/activate
        # Windows:
        venv\Scripts\activate

- Instale as dependencias:
        pip install -r requirements.txt


## Execução

- Execute o comando abaixo
        python main.py
        python main.py telegram (somente telegram)
        python main.py whatsApp (somente whatsApp)
