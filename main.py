from parser import *

opc: int = 0

print("| Opções:")
print("| 1 - Conversor de bases")
print("| 2 - Calculadora de Máximos")
print("| 3 - Modo Quiz")
print("| 4 - Sair")
print("~ ---------------------------------------------")

while opc != 4:
    opc = int(input("Insira uma das opções: "))
    if (opc > 4) or (opc < 1):
        print("\n| Opção inexistente! As opções são:")
        print("| 1 - Conversor de bases")
        print("| 2 - Calculadora de Máximos")
        print("| 3 - Modo Quiz")
        print("| 4 - Sair")
        print("~ ---------------------------------------------")

    match opc:
        case 1:
            print("Em desenvolvimento\n")
        case 2:
            print("Em desenvolvimento\n")
        case 3:
            print("Em desenvolvimento\n")

        case 4:
            print("Saindo...")



