# Instalação e Execução do Projeto

## Requisitos

- Python 3.10 ou superior (verifique com `python3 --version`)
- pip
- ngrok (apenas para o canal WhatsApp): https://ngrok.com/download
- Conta gratuita no Twilio (apenas para o canal WhatsApp)
- Token de bot do Telegram (gratuito, via [@BotFather](https://t.me/botfather))

## Instalação

Entre na pasta do projeto:

```bash
cd udesc-bot
```

Recomendado o uso de um ambiente virtual:

```bash
python3 -m venv venv

# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py            # roda Telegram + WhatsApp
python main.py telegram   # somente Telegram
python main.py whatsapp   # somente WhatsApp
```
