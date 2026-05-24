from conversor import *
from formatador import resposta_terminal, resposta_csv

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

def parser_calculadora() -> None:

    print("Insira o numero de Bits que deseja calcular o o maior valor representável nas 4 bases: ")

    nBits: int = int(input("Número de Bits: "))

    calculadora(nBits)

def parser_terminal() -> None:
    calcular: bool = True

    while calcular:
        
        calcular = False

        print("\n|Ao inserir a base você deve inserir o número correspondente a base, ou seja:"
              "\n|2 - Binário\n|8- Octal\n|10 - Decimal\n|16 - Hexadecimal")
        print("~ ---------------------------------------------")
        
        base_valor: bool = False
        while base_valor == False:
            valor = input("Insira o número: ")
            base_origem = int(input("Insira a base de origem: "))
            base_valor = validar_valor(valor, base_origem)
        
        base_destino = int(input("Insira a base de destino: "))
        
        resposta_terminal(base_origem, base_destino, valor)
        
        desejo_repetir = input("Deseja inserir outro número(s/N)? ") 

        # Repetimos apenas se for 's' pois a lógica aplicada 
        # é parecida com o terminal, qualquer coisa diferente de 's' é declarada como 'N' 
        if desejo_repetir == 's':
            calcular = True

    print('Saindo do modo Conversor de bases...')
           
    
def parser_csv(arquivo: str) -> None:
    import csv
    with open(f"{arquivo}.csv", "r", newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo, delimiter=";")
 
        for linha in leitor:
            resposta_csv(linha["valor"], linha["base_origem"], linha["base_destino"])
  
        arquivo.close()


