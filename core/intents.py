import re
import unicodedata

NUMERO_INTENCAO = {
    "1": "centros",
    "2": "sistemas_lista",
    "3": "id_udesc",
    "4": "sistemas_detalhe",
    "5": "cpf",
    "6": "tutoria",
    "7": "soe",
    "8": "residencia",
}

PALAVRAS_CHAVE = {
    "saudacao": [
        "ola",
        "oi",
        "bom dia",
        "boa tarde",
        "boa noite",
        "hello",
        "hi",
        "hey",
        "start",
        "iniciar",
    ],
    "menu": [
        "menu",
        "opcoes",
        "options",
        "ajuda",
        "help",
        "voltar",
        "back",
        "inicio",
        "home",
    ],
    "centros": [
        "centro",
        "centros",
        "endereco",
        "enderecos",
        "campus",
        "center",
        "address",
        "location",
        "onde fica",
    ],
    "sistemas_lista": [
        "siga",
        "moodle",
        "sigaa",
        "sistema",
        "sistemas",
        "system",
        "systems",
        "login",
        "acesso",
    ],
    "id_udesc": [
        "id udesc",
        "id-udesc",
        "idudesc",
        "identidade",
        "credencial",
        "credential",
        "usuario",
    ],
    "sistemas_detalhe": [
        "sas",
        "office",
        "365",
        "biblioteca",
        "library",
        "email",
        "e-mail",
        "teams",
        "word",
        "excel",
        "ppc",
        "calendario",
        "calendar",
    ],
    "cpf": [
        "cpf",
        "receita",
        "receita federal",
        "tax",
        "taxpayer",
        "documento",
        "document",
        "imposto",
    ],
    "tutoria": ["tutoria", "tutor", "tutoring", "mentoria", "mentor", "acolhimento"],
    "soe": [
        "soe",
        "orientacao",
        "psicologico",
        "psychological",
        "guidance",
        "apoio",
        "support",
        "sae",
    ],
    "residencia": [
        "residencia",
        "moradia",
        "alojamento",
        "housing",
        "dormitory",
        "casa",
        "morar",
        "rent",
        "aluguel",
    ],
}

IDIOMA = {
    "pt": ["pt", "portugues", "português", "portuguese", "br"],
    "en": ["en", "ingles", "inglês", "english", "us", "uk"],
}


def normalizar(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"\s+", " ", texto)
    return texto


def detectar_idioma(texto):
    texto_normalizado = normalizar(texto)
    for lang, termos in IDIOMA.items():
        if texto_normalizado in [normalizar(x) for x in termos]:
            return lang
    return None


def detectar_intencao(texto):
    texto_normalizado = normalizar(texto)

    if texto_normalizado in NUMERO_INTENCAO:
        return NUMERO_INTENCAO[texto_normalizado]

    for intent in ("saudacao", "menu"):
        for palavra_chave in PALAVRAS_CHAVE[intent]:
            if normalizar(palavra_chave) in texto_normalizado:
                return intent

    for intent, termos in PALAVRAS_CHAVE.items():
        if intent in ("saudacao", "menu"):
            continue
        for palavra_chave in termos:
            if normalizar(palavra_chave) in texto_normalizado:
                return intent

    return None
