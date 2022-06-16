import sys


# Requisito 12
def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    answers = [
        "Digite quantas notícias serão buscadas: ",
        "Digite o título: ",
        "Digite a data no formato aaaa-mm-dd: ",
        "Digite a fonte: ",
        "Digite a categoria "
    ]

    if not option or option > "7":
        sys.stderr.write("Opção inválida")

    for n in range(5):
        if option == str(n):
            input(answers[n])
