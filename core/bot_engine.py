from . import intents
from . import i18n
from . import menu_data as md

_SESSOES = {}

def _sessao(uid):
    if uid not in _SESSOES:
        _SESSOES[uid] = {"lang": "pt", "contexto": None}
    return _SESSOES[uid]


def _resp_lista_centros(lang):
    linhas = [i18n.t(lang, "choose_center")]
    for i, sigla in enumerate(md.ORDEM_CENTROS, start=1):
        c = md.CENTROS[sigla]
        linhas.append(f"{i} - {c['nome']} ({c['cidade']})")
    linhas.append("\n" + i18n.t(lang, "center_back"))
    return "\n".join(linhas)


def _resp_detalhe_centro(lang, indice):
    sigla = md.ORDEM_CENTROS[indice]
    c = md.CENTROS[sigla]
    rotulo_tel = "Telefone" if lang == "pt" else "Phone"
    return (f"*{c['nome']}*\n"
            f"{c['cidade']}\n"
            f"{c['endereco']}\n"
            f"{rotulo_tel}: {c['telefone']}\n"
            f"{c['url']}\n\n"
            f"{i18n.t(lang, 'center_back')}")


def _resp_lista_sistemas(lang, detalhe=False):
    cab = i18n.t(lang, "choose_system")
    linhas = [cab]
    for i, nome in enumerate(md.ORDEM_SISTEMAS, start=1):
        if detalhe:
            linhas.append(f"{i} - {md.SISTEMAS[lang][nome]}")
        else:
            linhas.append(f"{i} - {nome}")
    linhas.append("\n" + i18n.t(lang, "center_back"))
    return "\n".join(linhas)


def _resp_detalhe_sistema(lang, indice):
    nome = md.ORDEM_SISTEMAS[indice]
    return md.SISTEMAS[lang][nome] + "\n\n" + i18n.t(lang, "center_back")


def _resp_texto(lang, chave):
    return md.TEXTOS[lang][chave] + "\n\n" + i18n.t(lang, "center_back")


def _resp_menu(lang):
    return i18n.t(lang, "menu_header") + "\n" + i18n.menu(lang)


def _resp_boas_vindas(lang):
    return i18n.t(lang, "welcome") + "\n" + _resp_menu(lang)


def processar_mensagem(id_usuario, texto):
    """
    Recebe a mensagem de qualquer canal e devolve a resposta (string).
    id_usuario: identificador unico do usuario NO CANAL
    texto     : conteudo textual enviado pelo usuario.
    """
    
    if texto is None:
        texto = ""
    ses = _sessao(id_usuario)
    lang = ses["lang"]
    bruto = texto.strip()
    norm = intents.normalizar(bruto)

    novo_idioma = intents.detectar_idioma(bruto)
    if novo_idioma:
        ses["lang"] = novo_idioma
        ses["contexto"] = None
        return i18n.t(novo_idioma, "lang_changed") + "\n\n" + _resp_menu(novo_idioma)

    if ses["contexto"] == "centros" and norm.isdigit():
        idx = int(norm) - 1
        if 0 <= idx < len(md.ORDEM_CENTROS):
            ses["contexto"] = None
            return _resp_detalhe_centro(lang, idx)
    if ses["contexto"] in ("sistemas_lista", "sistemas_detalhe") and norm.isdigit():
        idx = int(norm) - 1
        if 0 <= idx < len(md.ORDEM_SISTEMAS):
            ses["contexto"] = None
            return _resp_detalhe_sistema(lang, idx)

    intent = intents.detectar_intencao(bruto)

    if intent == "saudacao":
        ses["contexto"] = None
        return _resp_boas_vindas(lang)

    if intent == "menu":
        ses["contexto"] = None
        return _resp_menu(lang)

    if intent == "centros":
        ses["contexto"] = "centros"
        return _resp_lista_centros(lang)

    if intent == "sistemas_lista":
        ses["contexto"] = "sistemas_lista"
        return _resp_lista_sistemas(lang, detalhe=False)

    if intent == "sistemas_detalhe":
        ses["contexto"] = "sistemas_detalhe"
        return _resp_lista_sistemas(lang, detalhe=True)

    if intent == "id_udesc":
        ses["contexto"] = None
        return _resp_texto(lang, "id_udesc")

    if intent == "cpf":
        ses["contexto"] = None
        return _resp_texto(lang, "cpf")

    if intent == "tutoria":
        ses["contexto"] = None
        return _resp_texto(lang, "tutoria")

    if intent == "soe":
        ses["contexto"] = None
        return _resp_texto(lang, "soe")

    if intent == "residencia":
        ses["contexto"] = None
        return _resp_texto(lang, "residencia")


    return i18n.t(lang, "not_understood") + "\n\n" + _resp_menu(lang)


if __name__ == "__main__":
    print("=== Modo teste local (digite 'sair' para encerrar) ===")
    print(processar_mensagem("local", "ola"))
    while True:
        try:
            msg = input("\nVoce > ")
        except (EOFError, KeyboardInterrupt):
            break
        if intents.normalizar(msg) in ("sair", "exit", "quit"):
            break
        print("Bot >", processar_mensagem("local", msg))
