from conversor import *
from formatador import resposta_terminal, resposta_csv
from quiz_core import *


def parser_geral() -> None:
    print("\n|Deseja passar os números via terminal ou arquivo '.csv'?")
    print("|1 - Terminal")
    print("|2 - Csv")
    print("~ ---------------------------------------------")

    opcao: int = int(input("Insira a opção: "))

    match opcao:
        case 1:
            parser_terminal()
        case 2:
            arquivo: str = input("Insira o nome do Arquivo: ")
            try:
                parser_csv(arquivo)
            except FileNotFoundError:
                print(f"O arquivo '{arquivo}.csv' não existe!")


def parser_calculadora() -> None:

    print("\n| Calculadora de máximos, apartir do número de bits.")
    print("~ ---------------------------------------------")

    nBits: int = int(input("Insira o número de bits: "))
    print("")

    calculadora(nBits)


def parser_quiz() -> None:

    print("\n| Bem-Vindo ao modo Quiz!")
    print("| Antes de começar uma breve explicação:")
    print("| No modo quiz, você seleciona uma dificuldade e quantas questões quer fazer, com aquela dificuldade,")
    print("| sendo que todas as questões envolvem conversão para diferentes bases.")
    print("| As dificuldades são em relação:")
    print("| - Ao número de tentativas, quanto mais dificil, menos tentativas")
    print("| - A quantidade de bits para o numero, ou seja, a faixa de numeros que pode ser representados com aqueles bits.")
    print("| - Ao número possuir vírgula ou não")
    print("| - Ao número possuir letras")
    print("| Dificuldades:")
    print("| 1 - Número de tentativas: 3 | Quantidade de bits para o numero: 3  | Sem números com vírgula    | Sem letras para os hexadecimais")
    print("| 2 - Número de tentativas: 3 | Quantidade de bits para o numero: 4  | Sem números com vírgula    | Possui letras para os hexadecimais")
    print("| 3 - Número de tentativas: 3 | Quantidade de bits para o numero: 8  | Sem números com vírgula    | Possui letras para os hexadecimais")
    print("| 4 - Número de tentativas: 2 | Quantidade de bits para o numero: 8  | Possui números com vírgula | Possui letras para os hexadecimais")
    print("| 5 - Número de tentativas: 1 | Quantidade de bits para o numero: 12 | Possui números com vírgula | Possui letras para os hexadecimais")
    print("~ ---------------------------------------------")

    dificuldade: int = int(input("Insira a dificuldade: "))
    num_questoes: int = int(input("Insira o número de questões: "))

    pontuacao = quiz_start(dificuldade, num_questoes)

    print(f"Sua pontuação total foi: {pontuacao}/{num_questoes}")


def parser_terminal() -> None:
    continuar_calculando: bool = True

    desejo_passos: str = input("Deseja que seja mostrado um passo a passo da solução(s/N)?")
    passos: bool = False
    if desejo_passos == 's':
        passos = True

    while continuar_calculando:

        continuar_calculando = False

        print("\n|Ao inserir a base você deve inserir o número correspondente a base, ou seja:"
              "\n|2 - Binário\n|8- Octal\n|10 - Decimal\n|16 - Hexadecimal")
        print("~ ---------------------------------------------")

        base_valor: bool = False
        while base_valor is False:
            valor_converter: str = input("Insira o número: ")
            base_origem: int = int(input("Insira a base de origem: "))
            base_valor = validar_valor(valor_converter, base_origem)

        base_destino: int = int(input("Insira a base de destino: "))
        print("")

        valor_convertido: int = valor_converter
        if base_origem != base_destino:
            valor_convertido = resposta_terminal(base_origem, base_destino, valor_converter, passos)

        print(f"Resposta final: {valor_convertido} \n")

        desejo_repetir = input("Deseja inserir outro número(s/N)? ")

        # Repetimos apenas se for 's' pois a lógica aplicada
        # é parecida com o terminal, qualquer coisa diferente de 's' é declarada como 'N'
        if desejo_repetir == 's':
            continuar_calculando = True

    print('Saindo do modo Conversor de bases...')


def parser_csv(arquivo_nome: str) -> None:

    import csv

    with open("saida.csv", "w", newline="", encoding="utf-8") as arquivo:

        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(["valor", "base_origem", "resposta", "base_destino"])

    arquivo.close()

    with open(f"{arquivo_nome}.csv", "r", newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            resposta_csv(linha["valor"], linha["base_origem"], linha["base_destino"])

        arquivo.close()

    print("Respostas salvas em 'saida.csv'")
