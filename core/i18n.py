MENU_PRINCIPAL = {
    "pt": (
        "1 - Enderecos dos Centros da UDESC\n"
        "2 - Sistemas que voce vai usar (SIGA, Moodle, SIGAA)\n"
        "3 - Como obter o ID UDESC\n"
        "4 - Sistemas UDESC (detalhes: SAS, Office 365, Biblioteca...)\n"
        "5 - Voce precisa de um CPF (Receita Federal)\n"
        "6 - Equipe de Tutoria\n"
        "7 - SOE - Servico de Orientacao ao Estudante\n"
        "8 - Residencia estudantil / moradia\n"
        "\nDigite o numero da opcao, ou 'menu' para ver isto de novo.\n"
        "Para trocar o idioma digite: en (English) | pt (Portugues)"
    ),
    "en": (
        "1 - UDESC Centers addresses\n"
        "2 - Systems you will use (SIGA, Moodle, SIGAA)\n"
        "3 - How to get your UDESC ID\n"
        "4 - UDESC systems (details: SAS, Office 365, Library...)\n"
        "5 - You need a CPF (Federal Revenue)\n"
        "6 - Tutoring team\n"
        "7 - SOE - Student Guidance Service\n"
        "8 - Student housing\n"
        "\nType the option number, or 'menu' to see this again.\n"
        "To change language type: en (English) | pt (Portuguese)"
    ),
}

UI = {
    "pt": {
        "welcome": (
            "Ola! Bem-vindo(a) a UDESC! \U0001f44b\n"
            "Sou o assistente virtual para estudantes de intercambio. "
            "Posso ajudar com sistemas, documentos, tutoria e mais.\n"
        ),
        "menu_header": "*Menu principal*",
        "choose_center": "Escolha um centro digitando o numero:",
        "choose_system": "Escolha um sistema digitando o numero:",
        "center_back": "Digite 'menu' para voltar ao menu principal.",
        "lang_changed": "Idioma alterado para Portugues. \U0001f1e7\U0001f1f7",
        "invalid_option": "Opcao invalida. Escolha um numero da lista.",
        "not_understood": (
            "Desculpe, nao entendi. \U0001f914\n"
            "Digite 'menu' para ver as opcoes, ou um numero de 1 a 8."
        ),
        "llm_prefix": "",
    },
    "en": {
        "welcome": (
            "Hello! Welcome to UDESC! \U0001f44b\n"
            "I'm the virtual assistant for exchange students. I can help with "
            "systems, documents, tutoring and more.\n"
        ),
        "menu_header": "*Main menu*",
        "choose_center": "Choose a center by typing its number:",
        "choose_system": "Choose a system by typing its number:",
        "center_back": "Type 'menu' to go back to the main menu.",
        "lang_changed": "Language changed to English. \U0001f1fa\U0001f1f8",
        "invalid_option": "Invalid option. Please choose a number from the list.",
        "not_understood": (
            "Sorry, I didn't understand. \U0001f914\n"
            "Type 'menu' to see the options, or a number from 1 to 8."
        ),
        "llm_prefix": "",
    },
}


def t(lang, key):
    return UI.get(lang, UI["pt"]).get(key, UI["pt"].get(key, ""))


def menu(lang):
    return MENU_PRINCIPAL.get(lang, MENU_PRINCIPAL["pt"])
