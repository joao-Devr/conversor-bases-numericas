from parser import parser_geral, parser_calculadora

opcao: int = 0

while opcao != 4:

    print("| Opções:")
    print("| 1 - Conversor de bases")
    print("| 2 - Calculadora de Máximos")
    print("| 3 - Modo Quiz")
    print("| 4 - Sair")
    print("~ ---------------------------------------------")
    
    opcao = int(input("Insira uma das opções: "))

    match opcao:
        case 1:
            parser_geral()
            print("")
        case 2:
            parser_calculadora()
            print("")
        case 3:
            print("Em desenvolvimento\n")
        case 4:
            print("Saindo...")
        case _:         
            print("\n| Opção inexistente!")

