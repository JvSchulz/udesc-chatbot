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
        centro = md.CENTROS[sigla]
        linhas.append(f"{i} - {centro['nome']} ({centro['cidade']})")
    linhas.append("\n" + i18n.t(lang, "center_back"))
    return "\n".join(linhas)


def _resp_detalhe_centro(lang, indice):
    sigla = md.ORDEM_CENTROS[indice]
    centro = md.CENTROS[sigla]
    rotulo_tel = "Telefone" if lang == "pt" else "Phone"
    return (
        f"*{centro['nome']}*\n"
        f"{centro['cidade']}\n"
        f"{centro['endereco']}\n"
        f"{rotulo_tel}: {centro['telefone']}\n"
        f"{centro['url']}\n\n"
        f"{i18n.t(lang, 'center_back')}"
    )


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
    sessao = _sessao(id_usuario)
    lang = sessao["lang"]
    bruto = texto.strip()
    intencao_normalizada = intents.normalizar(bruto)

    novo_idioma = intents.detectar_idioma(bruto)
    if novo_idioma:
        sessao["lang"] = novo_idioma
        sessao["contexto"] = None
        return i18n.t(novo_idioma, "lang_changed") + "\n\n" + _resp_menu(novo_idioma)

    if sessao["contexto"] == "centros" and intencao_normalizada.isdigit():
        idx = int(intencao_normalizada) - 1
        if 0 <= idx < len(md.ORDEM_CENTROS):
            sessao["contexto"] = None
            return _resp_detalhe_centro(lang, idx)
    if (
        sessao["contexto"] in ("sistemas_lista", "sistemas_detalhe")
        and intencao_normalizada.isdigit()
    ):
        idx = int(intencao_normalizada) - 1
        if 0 <= idx < len(md.ORDEM_SISTEMAS):
            sessao["contexto"] = None
            return _resp_detalhe_sistema(lang, idx)

    intent = intents.detectar_intencao(bruto)

    if intent == "saudacao":
        sessao["contexto"] = None
        return _resp_boas_vindas(lang)

    if intent == "menu":
        sessao["contexto"] = None
        return _resp_menu(lang)

    if intent == "centros":
        sessao["contexto"] = "centros"
        return _resp_lista_centros(lang)

    if intent == "sistemas_lista":
        sessao["contexto"] = "sistemas_lista"
        return _resp_lista_sistemas(lang, detalhe=False)

    if intent == "sistemas_detalhe":
        sessao["contexto"] = "sistemas_detalhe"
        return _resp_lista_sistemas(lang, detalhe=True)

    if intent == "id_udesc":
        sessao["contexto"] = None
        return _resp_texto(lang, "id_udesc")

    if intent == "cpf":
        sessao["contexto"] = None
        return _resp_texto(lang, "cpf")

    if intent == "tutoria":
        sessao["contexto"] = None
        return _resp_texto(lang, "tutoria")

    if intent == "soe":
        sessao["contexto"] = None
        return _resp_texto(lang, "soe")

    if intent == "residencia":
        sessao["contexto"] = None
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
