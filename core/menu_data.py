
CENTROS = {
    "CCT": {
        "nome": "CCT - Centro de Ciencias Tecnologicas",
        "cidade": "Joinville/SC",
        "endereco": "Rua Paulo Malschitzki, 200 - Zona Industrial Norte - "
                    "Joinville/SC - CEP 89.219-710",
        "telefone": "(47) 3481-7900",
        "url": "https://www.udesc.br/cct",
    },
    "ESAG": {
        "nome": "ESAG - Centro de Ciencias da Administracao e Socioeconomicas",
        "cidade": "Florianopolis/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "(48) 3664-8000",  # VERIFICAR (telefone geral da UDESC)
        "url": "https://www.udesc.br/esag",
    },
    "CAV": {
        "nome": "CAV - Centro de Ciencias Agroveterinarias",
        "cidade": "Lages/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "Consultar no site oficial",  # VERIFICAR
        "url": "https://www.udesc.br/cav",
    },
    "CEART": {
        "nome": "CEART - Centro de Artes, Design e Moda",
        "cidade": "Florianopolis/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "Consultar no site oficial",  # VERIFICAR
        "url": "https://www.udesc.br/ceart",
    },
    "CEFID": {
        "nome": "CEFID - Centro de Ciencias da Saude e do Esporte",
        "cidade": "Florianopolis/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "Consultar no site oficial",  # VERIFICAR
        "url": "https://www.udesc.br/cefid",
    },
    "FAED": {
        "nome": "FAED - Centro de Ciencias Humanas e da Educacao",
        "cidade": "Florianopolis/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "Consultar no site oficial",  # VERIFICAR
        "url": "https://www.udesc.br/faed",
    },
    "CEAVI": {
        "nome": "CEAVI - Centro de Educacao Superior do Alto Vale do Itajai",
        "cidade": "Ibirama/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "(47) 3357-8484",
        "url": "https://www.udesc.br/ceavi",
    },
    "CEO": {
        "nome": "CEO - Centro de Educacao Superior do Oeste",
        "cidade": "Chapeco/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "Consultar no site oficial",  # VERIFICAR
        "url": "https://www.udesc.br/ceo",
    },
    "CEPLAN": {
        "nome": "CEPLAN - Centro de Educacao do Planalto Norte",
        "cidade": "Sao Bento do Sul/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "Consultar no site oficial",  # VERIFICAR
        "url": "https://www.udesc.br/ceplan",
    },
    "CERES": {
        "nome": "CERES - Centro de Educacao Superior da Regiao Sul",
        "cidade": "Laguna/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "Consultar no site oficial",  # VERIFICAR
        "url": "https://www.udesc.br/ceres",
    },
    "CESFI": {
        "nome": "CESFI - Centro de Educacao Superior da Foz do Itajai",
        "cidade": "Balneario Camboriu/SC",
        "endereco": "Consultar no site oficial",  # VERIFICAR
        "telefone": "Consultar no site oficial",  # VERIFICAR
        "url": "https://www.udesc.br/cesfi",
    },
    "CEAD": {
        "nome": "CEAD - Centro de Educacao a Distancia",
        "cidade": "Florianopolis/SC",
        "endereco": "Av. Madre Benvenuta, 2007 - Itacorubi - "
                    "Florianopolis/SC - CEP 88.035-901",
        "telefone": "(48) 3664-8402",
        "url": "https://www.udesc.br/cead",
    },
}

ORDEM_CENTROS = ["CCT", "ESAG", "CAV", "CEART", "CEFID", "FAED",
                 "CEAVI", "CEO", "CEPLAN", "CERES", "CESFI", "CEAD"]


SISTEMAS = {
    "pt": {
        "SIGA": "SIGA - Sistema de gestao academica: consulta de notas, "
                "faltas, matriculas e situacao academica. Acesso com o ID "
                "UDESC. https://www.udesc.br (busque por 'SIGA').",
        "Moodle": "Moodle - Ambiente Virtual de Aprendizagem (AVA): "
                  "disciplinas, materiais, entrega de exercicios e provas "
                  "online. Acesso com o ID UDESC.",
        "SIGAA": "SIGAA - Sistema de gestao academica usado em alguns modulos "
                 "da UDESC. Acesso com o ID UDESC.",
        "Site UDESC": "Site UDESC - Informacoes institucionais: Plano de "
                      "Curso (PPC), corpo docente, calendario academico.",
        "SAS": "SAS - Agendamento e verificacao de reservas de salas.",
        "Office 365": "Office 365 - E-mail institucional e aplicativos "
                      "Microsoft (Word, Excel, Teams, etc.).",
        "Biblioteca": "Biblioteca online - Busca de livros e repositorio de "
                      "TCCs, dissertacoes e teses (Pergamum/BU UDESC).",
    },
    "en": {
        "SIGA": "SIGA - Academic management system: grades, absences, "
                "enrollment and academic status. Login with your UDESC ID.",
        "Moodle": "Moodle - Virtual Learning Environment: courses, materials, "
                  "assignment submission and online exams. Login with UDESC ID.",
        "SIGAA": "SIGAA - Academic management system used in some UDESC "
                 "modules. Login with your UDESC ID.",
        "Site UDESC": "UDESC website - Institutional information: course plan "
                      "(PPC), faculty, academic calendar.",
        "SAS": "SAS - Room booking and reservation check.",
        "Office 365": "Office 365 - Institutional e-mail and Microsoft apps "
                      "(Word, Excel, Teams, etc.).",
        "Biblioteca": "Online library - Book search and repository of theses "
                      "and dissertations (Pergamum/UDESC Library).",
    },
}
ORDEM_SISTEMAS = ["SIGA", "Moodle", "SIGAA", "Site UDESC", "SAS",
                  "Office 365", "Biblioteca"]


TEXTOS = {
    "pt": {
        "id_udesc": (
            "*Como obter o ID UDESC*\n"
            "1) Acesse o portal de identidade da UDESC (id.udesc.br ou link "
            "indicado pela secretaria academica do seu centro).\n"
            "2) Informe seu numero de matricula e dados pessoais.\n"
            "3) Crie sua senha e valide o e-mail institucional.\n"
            "Em caso de duvida, procure a Secretaria Academica ou a equipe "
            "de tutoria do seu centro."
        ),
        "cpf": (
            "*Voce precisa de um CPF*\n"
            "O CPF (Cadastro de Pessoa Fisica) e necessario para abrir conta, "
            "fazer contratos e muitos servicos no Brasil.\n"
            "1) Solicite online no site da Receita Federal "
            "(www.gov.br/receitafederal) - opcao para estrangeiros.\n"
            "2) O estrangeiro deve comparecer PRESENCIALMENTE a uma unidade da "
            "Receita Federal para validar o CPF, levando passaporte e "
            "documentos de identificacao.\n"
            "Unidade da Receita Federal mais proxima do seu centro: use o "
            "menu de centros para ver o endereco da sua cidade e procure a "
            "agencia local da Receita Federal."
        ),
        "tutoria": (
            "*Equipe de Tutoria Academica*\n"
            "A tutoria acolhe e orienta estudantes,inclusive estrangeiros.\n"
            "CCT - Tutoria Academica:\n"
            "Site: https://www.udesc.br/cct/tutoriaacademica\n"
            "Equipe: https://www.udesc.br/cct/tutoriaacademica/equipe\n"
            "E-mail: tutoria.cct@udesc.br\n"
            "Supervisora TADS: Profa. Debora Cabral Nazario\n"
            "Supervisora Ciencia da Computacao: Profa. Luciana Rita Guedes"
        ),
        "soe": (
            "*SOE - Servico de Orientacao ao Estudante*\n"
            "O SOE oferece apoio psicologico, pedagogico e social ao "
            "estudante.\n"
            "Procure a Secretaria de Assuntos Estudantis (SAE) ou a "
            "coordenacao do seu centro para horarios e agendamento.\n"
            "Site institucional: https://www.udesc.br (busque por 'SAE' ou "
            "'SOE')."
        ),
        "residencia": (
            "*Residencia Estudantil / Moradia*\n"
            "A disponibilidade de residencia estudantil varia conforme o "
            "centro. Nem todos os centros possuem moradia propria, e o "
            "atendimento a estrangeiros depende de edital.\n"
            "Procure a SAE (Secretaria de Assuntos Estudantis) e a tutoria do "
            "seu centro para verificar editais de moradia e auxilio."
        ),
    },
    "en": {
        "id_udesc": (
            "*How to get your UDESC ID*\n"
            "The UDESC ID is your unique login for all systems.\n"
            "1) Go to the UDESC identity portal (id.udesc.br or the link given "
            "by your center's academic office).\n"
            "2) Enter your enrollment number and personal data.\n"
            "3) Create your password and validate your institutional e-mail.\n"
            "If you have trouble, contact the Academic Office or the tutoring "
            "team of your center."
        ),
        "cpf": (
            "*You need a CPF*\n"
            "The CPF (Brazilian individual taxpayer registry) is required to "
            "open a bank account, sign contracts and use many services.\n"
            "1) Request it online at the Federal Revenue website "
            "(www.gov.br/receitafederal) - foreigner option.\n"
            "2) Foreigners must go IN PERSON to a Federal Revenue office to "
            "validate the CPF, bringing passport and ID documents.\n"
            "Use the centers menu to find the address of your city and look "
            "for the local Federal Revenue (Receita Federal) office."
        ),
        "tutoria": (
            "*Academic Tutoring Team*\n"
            "Tutoring welcomes and guides students (including foreigners).\n"
            "CCT - Academic Tutoring:\n"
            "Site: https://www.udesc.br/cct/tutoriaacademica\n"
            "Team: https://www.udesc.br/cct/tutoriaacademica/equipe\n"
            "E-mail: tutoria.cct@udesc.br\n"
            "TADS supervisor: Prof. Debora Cabral Nazario\n"
            "Computer Science supervisor: Prof. Luciana Rita Guedes"
        ),
        "soe": (
            "*SOE - Student Guidance Service*\n"
            "SOE offers psychological, pedagogical and social support to "
            "students.\n"
            "Contact the Student Affairs Office (SAE) or your center's "
            "coordination for schedules and appointments.\n"
            "Website: https://www.udesc.br (search for 'SAE' or 'SOE')."
        ),
        "residencia": (
            "*Student Housing*\n"
            "Student housing availability varies by center. Not every center "
            "has its own housing, and service to foreigners depends on a "
            "public call (edital).\n"
            "Contact the Student Affairs Office (SAE) and your center's "
            "tutoring team to check housing and support calls."
        ),
    },
}
