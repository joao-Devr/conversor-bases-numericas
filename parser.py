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
            parser_terminal()
        case 2:
            arquivo: str = input("Insira o nome do Arquivo: ")
            try:
                parser_csv(arquivo)
            except FileNotFoundError:
                print(f"O arquivo '{arquivo}.csv' não existe!")

def parser_calculadora() -> None:
    
    print("")
    print("| Calculadora de máximos, apartir do número de bits.")
    print("~ ---------------------------------------------")

    nBits: int = int(input("Insira o número de bits: "))
    print("")

    calculadora(nBits)

def parser_terminal() -> None:
    calcular: bool = True

    desejo_passos: str = input("Deseja que seja mostrado um passo a passo da solução(s/N)?")
    passos: bool = False
    if desejo_passos == 's':
        passos = True

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
        print("")
        
        resposta_terminal(base_origem, base_destino, valor, passos)
        
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


