import sys
import time
import requests

try:
    from core import bot_engine
    import config
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from core import bot_engine
    import config

API = "https://api.telegram.org/bot{token}/{method}"

def _chamar(method, token, **params):
    url = API.format(token=token, method=method)
    try:
        r = requests.get(url, params=params, timeout=40)
        return r.json()
    except requests.RequestException as e:
        print(f"[telegram] erro de rede: {e}")
        return None


def enviar_mensagem(token, chat_id, texto):
    resp = _chamar("sendMessage", token, chat_id=chat_id, text=texto, parse_mode="Markdown")
    if resp and not resp.get("ok"):
        print(f"[telegram] Markdown falhou, reenviando sem formatacao")
        resp = _chamar("sendMessage", token, chat_id=chat_id, text=texto)
    return resp


def run(token=None):
    token = token or config.TELEGRAM_TOKEN
    if not token:
        print("ERRO: defina TELEGRAM_TOKEN (veja README.txt). Encerrando.")
        return

    me = _chamar("getMe", token)
    if not me or not me.get("ok"):
        print("ERRO: token invalido ou sem rede. Resposta:", me)
        return
    print(f"[telegram] Bot @{me['result'].get('username')} online. "
          f"Aguardando mensagens (Ctrl+C para sair)...")

    offset = None
    while True:
        updates = _chamar("getUpdates", token, timeout=30, offset=offset)
        if not updates or not updates.get("ok"):
            time.sleep(2)
            continue

        for upd in updates["result"]:
            offset = upd["update_id"] + 1
            msg = upd.get("message") or upd.get("edited_message")
            if not msg:
                continue
            chat_id = msg["chat"]["id"]
            texto = msg.get("text", "")

            resposta = bot_engine.processar_mensagem(f"tg:{chat_id}", texto)
            enviar_mensagem(token, chat_id, resposta)
            print(f"[telegram] {chat_id}: {texto!r} -> respondido")


if __name__ == "__main__":
    run()
