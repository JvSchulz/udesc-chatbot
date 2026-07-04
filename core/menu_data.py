# -*- coding: utf-8 -*-
"""
menu_data.py
------------
Base de conhecimento do chatbot: conteudo dos menus exigidos pela Tabela 1 do
enunciado, em portugues (pt) e ingles (en).

IMPORTANTE PARA A BANCA / EQUIPE
--------------------------------
Os dados abaixo foram coletados do portal oficial da UDESC (www.udesc.br) em
junho/2026. Os campos marcados com "" devem ser confirmados com a
equipe de tutoria do CCT antes da entrega, pois enderecos e telefones de alguns
centros podem mudar. O enunciado autoriza entrevistas com a tutoria justamente
para isso (Secao "Observacao" da Tabela 1).

A estrutura e propositalmente um dicionario "burro" (so dados). Toda a logica de
navegacao fica em intents.py / bot_engine.py. Isso mantem o conteudo separado do
codigo (principio de separacao de responsabilidades), o que facilita traduzir,
auditar e atualizar as informacoes sem mexer na logica do bot.
"""

# ---------------------------------------------------------------------------
# 1) CENTROS DE ENSINO DA UDESC
# Fonte: https://www.udesc.br/sobreoscentros (12 centros oficiais)
# O CCT (onde o trabalho e apresentado) esta com a ficha completa; os demais
# trazem nome, cidade e URL oficial (padrao real udesc.br/<sigla>).
# ---------------------------------------------------------------------------
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
        "endereco": "Av. Me. Benvenuta, 2037 - Itacorubi, Florianópolis - SC, 88035-001",
        "telefone": "(48) 3664-8200",
        "url": "https://www.udesc.br/esag",
    },
    "CAV": {
        "nome": "CAV - Centro de Ciencias Agroveterinarias",
        "cidade": "Lages/SC",
        "endereco": "Av. Luiz de Camões, 2090 - Conta Dinheiro, Lages - SC, 88520-000",
        "telefone": "(49) 3289-9100",
        "url": "https://www.udesc.br/cav",
    },
    "CEART": {
        "nome": "CEART - Centro de Artes, Design e Moda",
        "cidade": "Florianopolis/SC",
        "endereco": "Av. Me. Benvenuta, 1907 - Itacorubi, Florianópolis - SC, 88035-901",  
        "telefone": "(48) 3664-8300",  
        "url": "https://www.udesc.br/ceart",
    },
    "CEFID": {
        "nome": "CEFID - Centro de Ciencias da Saude e do Esporte",
        "cidade": "Florianopolis/SC",
        "endereco": "R. Pascoal Simone, 358 - Coqueiros, Florianópolis - SC, 88080-350",  
        "telefone": "(48) 3664-8600",  
        "url": "https://www.udesc.br/cefid",
    },
    "FAED": {
        "nome": "FAED - Centro de Ciencias Humanas e da Educacao",
        "cidade": "Florianopolis/SC",
        "endereco": "Servidão Caminho do Pôrto, 1 - Itacorubi, Florianópolis - SC, 88034-257",  
        "telefone": "(48) 3321-8500",  
        "url": "https://www.udesc.br/faed",
    },
    "CEAVI": {
        "nome": "CEAVI - Centro de Educacao Superior do Alto Vale do Itajai",
        "cidade": "Ibirama/SC",
        "endereco": "R. Dr. Getúlio Vargas, 2822 - Bela Vista, Ibirama - SC, 89140-000",  
        "telefone": "(47) 3357-8484",
        "url": "https://www.udesc.br/ceavi",
    },
    "CEO": {
        "nome": "CEO - Centro de Educacao Superior do Oeste",
        "cidade": "Chapeco/SC",
        "endereco": "R. Beloni Trombeta Zanin, 680E - Santo Antônio, Chapecó - SC, 89815-630",  
        "telefone": "(49) 2049-9524",  
        "url": "https://www.udesc.br/ceo",
    },
    "CEPLAN": {
        "nome": "CEPLAN - Centro de Educacao do Planalto Norte",
        "cidade": "Sao Bento do Sul/SC",
        "endereco": "R. Luiz Fernando Hastreiter, 180 - Centenário, São Bento do Sul - SC, 89283-081",  
        "telefone": "(47) 3647-0074",  
        "url": "https://www.udesc.br/ceplan",
    },
    "CERES": {
        "nome": "CERES - Centro de Educacao Superior da Regiao Sul",
        "cidade": "Laguna/SC",
        "endereco": "R. Cel. Fernandes Martins, 270 - Progresso, Laguna - SC, 88790-000",  
        "telefone": "(48) 3647-7900",  
        "url": "https://www.udesc.br/ceres",
    },
    "CESFI": {
        "nome": "CESFI - Centro de Educacao Superior da Foz do Itajai",
        "cidade": "Balneario Camboriu/SC",
        "endereco": "Avenida Lourival Cesario Pereira, s/n Edificio Alcides Abreu - Nova Esperança, Balneário Camboriú - SC, 88336-275",  
        "telefone": "(47) 3398-6592",  
        "url": "https://www.udesc.br/cesfi",
    },
    "CEAD": {
        "nome": "CEAD - Centro de Educacao a Distancia",
        "cidade": "Florianopolis/SC",
        "endereco": "Av. Madre Benvenuta, 2007 - Itacorubi - "
                    "Florianopolis/SC - CEP 88.035-901",
        "telefone": "(48) 3664-8400",
        "url": "https://www.udesc.br/cead",
    },
}

# Ordem fixa de exibicao (CCT primeiro por ser o centro da apresentacao).
ORDEM_CENTROS = ["CCT", "ESAG", "CAV", "CEART", "CEFID", "FAED",
                 "CEAVI", "CEO", "CEPLAN", "CERES", "CESFI", "CEAD"]


# ---------------------------------------------------------------------------
# 2) SISTEMAS DA UDESC (item 2 e 4 da Tabela 1)
# ---------------------------------------------------------------------------
SISTEMAS = {
    "pt": {
        "SIGA": "SIGA - Sistema de gestao academica: consulta de notas, "
                "faltas, matriculas e situacao academica. Acesso com o ID "
                "UDESC. https://siga.udesc.br.",
        "Moodle": "Moodle: "
                  "disciplinas, materiais, entrega de exercicios e provas "
                  "online. Acesso com o ID UDESC. https://www.udesc.br/<SEU_CENTRO>/calouros/moodle",
        "SIGAA": "SIGAA - Sistema de gestao academica usado em alguns modulos "
                 "da UDESC. Acesso com o ID UDESC. https://www.udesc.br/sistema/sigaa",
        "Site UDESC": "Site UDESC - Informacoes institucionais: Plano de "
                      "Curso (PPC), corpo docente, calendario academico. https://www.udesc.br",
        "SAS": "SAS - Agendamento e verificacao de reservas de salas. https://sas.sistemas.udesc.br",
        "Office 365": "Office 365 - E-mail institucional e aplicativos "
                      "Microsoft (Word, Excel, Teams, etc.). https://www.udesc.br/sistemas/office365",
        "Biblioteca": "Biblioteca online - Busca de livros e repositorio de "
                      "TCCs, dissertacoes e teses (Pergamum/BU UDESC). https://www.udesc.br/bu",
    },
    "en": {
        "SIGA": "SIGA - Academic management system: grades, absences, "
                "enrollment and academic status. Login with your UDESC ID. https://siga.udesc.br",
        "Moodle": "Moodle - Virtual Learning Environment: courses, materials, "
                  "assignment submission and online exams. Login with UDESC ID. https://www.udesc.br/<SEU_CENTRO>/calouros/moodle",
        "SIGAA": "SIGAA - Academic management system used in some UDESC "
                 "modules. Login with your UDESC ID. https://www.udesc.br/sistema/sigaa",
        "Site UDESC": "UDESC website - Institutional information: course plan "
                      "(PPC), faculty, academic calendar. https://www.udesc.br",
        "SAS": "SAS - Room booking and reservation check. https://sas.sistemas.udesc.br",
        "Office 365": "Office 365 - Institutional e-mail and Microsoft apps "
                      "(Word, Excel, Teams, etc.).",
        "Biblioteca": "Online library - Book search and repository of theses https://www.udesc.br/sistemas/office365"
                      "and dissertations (Pergamum/UDESC Library). https://www.udesc.br/bu",
    },
}
ORDEM_SISTEMAS = ["SIGA", "Moodle", "SIGAA", "Site UDESC", "SAS",
                  "Office 365", "Biblioteca"]


# ---------------------------------------------------------------------------
# 3) TEXTOS DOS DEMAIS ITENS DA TABELA 1 (3, 5, 6, 7, 8)
# Bilingue. Conteudo institucional baseado no portal UDESC e na CCT.
# ---------------------------------------------------------------------------
TEXTOS = {
    "pt": {
        "id_udesc": (
            "*Como obter o ID UDESC*\n"
            "O ID UDESC e a sua identidade unica de acesso aos sistemas.\n"
            "1) Acesse o site: Entre no portal id.udesc.br. \n"
            "2) Respeite o prazo: Faça isso a partir do dia seguinte à sua matrícula. \n"
            "3) Inicie o processo: Clique na opção 'Primeiro acesso' \n"
            "4) Informe seus dados: Digite apenas os números do seu CPF. \n"
            "5) Confirme no e-mail: Siga as instruções enviadas para o seu e-mail cadastrado. \n"
            "Em caso de duvida, procure a Secretaria Academica ou a equipe de tutoria do seu centro."
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
            "A tutoria acolhe e orienta estudantes (inclusive estrangeiros).\n"
            "CCT - Tutoria Academica:\n"
            "Site: https://www.udesc.br/cct/tutoriaacademica \n"
            "Equipe: https://www.udesc.br/cct/tutoriaacademica/equipe \n"
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
            "Site institucional: https://www.udesc.br/cct/soe."  
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
