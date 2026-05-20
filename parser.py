from conversor import *

def parser_geral() -> None:
    print("\n|Deseja passar os números via terminal ou arquivo '.csv'?")
    print("|1 - Terminal")
    print("|2 - Csv")
    print("~ ---------------------------------------------")

    opcao:int  = int(input("Insira a opção: "))

    match opcao:
        case 1:
            parse_terminal()
        case 2:
            arquivo: str = input("Insira o nome do Arquivo: ")
            try:
                parse_csv(arquivo)
            except FileNotFoundError:
                print(f"O arquivo '{arquivo}.csv' não existe!")

def parse_terminal() -> None:
    from formatador import resposta_terminal
    calcular: bool = True

    while calcular:

        print("\n|Ao inserir a base você deve inserir o número correspondente a base, ou seja:"
              "\n|2 - Binário\n|8- Octal\n|10 - Decimal\n|16 - Hexadecimal")
        print("~ ---------------------------------------------")
        
        base_valor: bool = False
        while base_valor == False:
            base_origem = input("Insira a base de origem: ")
            valor = input("Insira o número: ")
            base_valor = validar_valor(valor, int(base_origem))
        base_destino = input("Insira a base de destino: ")
        
        desejo_repetir = input("Deseja inserir outro número(s/N)? ")
        if desejo_repetir == 'N':
            resposta_terminal(base_origem, base_destino, valor)
            calcular = False
        elif desejo_repetir == 's':
            resposta_terminal(base_origem, base_destino, valor)
            calcular = True        
    
def parse_csv(arquivo: str) -> None:
    import csv
    from formatador import resposta_csv
    with open(f"{arquivo}.csv", "r", newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo, delimiter=";")
 
        for linha in leitor:
            resposta_csv(linha["valor"], linha["base_origem"], linha["base_destino"])
  
        arquivo.close()
