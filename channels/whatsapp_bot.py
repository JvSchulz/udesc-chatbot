import sys
import logging

try:
    from flask import Flask, request, Response
    from twilio.twiml.messaging_response import MessagingResponse
except ImportError:
    print("ERRO: instale as dependencias -> pip install flask twilio")
    raise

try:
    from core import bot_engine
    import config
except ImportError:
    import os

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from core import bot_engine
    import config

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    ip_destino_local = request.environ.get("SERVER_NAME")
    porta_destino = request.environ.get("SERVER_PORT")
    ip_origem = request.remote_addr
    porta_origem = request.environ.get("REMOTE_PORT")
    logging.info(f"Telegram - Local: IP {ip_origem} / Porta {porta_origem}")
    logging.info(f"Telegram - Externo: IP {ip_destino_local} / Porta {porta_destino}")
    return "Chatbot UDESC Intercambio (WhatsApp/Twilio) esta no ar.", 200


@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    texto = request.form.get("Body", "")
    remetente = request.form.get("From", "desconhecido")

    resposta = bot_engine.processar_mensagem(f"wa:{remetente}", texto)

    twiml = MessagingResponse()
    twiml.message(resposta)
    print(f"[whatsapp] {remetente}: {texto!r} -> respondido")
    return Response(str(twiml), mimetype="application/xml")


def run(port=None):
    port = port or config.WHATSAPP_PORT
    print(f"[whatsapp] Servidor Flask escutando na porta {port}")
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)


if __name__ == "__main__":
    run()
