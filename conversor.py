tabela_hexadecimal: list[str] = [
        '0', '1', '2', '3', '4', '5',
        '6', '7', '8', '9', 'A', 'B',
        'C', 'D', 'E', 'F'
        ]
tabela_binario: list[str] = [
        '0000', '0001', '0010', '0011', '0100',
        '0101', '0110', '0111', '1000', '1001',
        '1010', '1011', '1100', '1101', '1110', '1111'
        ]


def validar_valor(numero: str, base_origem: int) -> bool:
    simbolos_permitidos = tabela_hexadecimal[:base_origem]
    simbolos_permitidos.append('.')

    for simbolo_inserido in numero:
        existe_simbolo: bool = False

        if simbolo_inserido in simbolos_permitidos:
            existe_simbolo = True

        if existe_simbolo is False:
            print(f"O simbolo '{simbolo_inserido}' não pertence a base {base_origem} \n")
            return False

    return True


def binario_ho(valor_converter: str, base_destino: int, passos: bool = False) -> str:

    pos_virgula: int = valor_converter.find('.')

    antes_virgula: str = valor_converter
    depois_virgula: str = ''
    trecho_extra_pos_virgula: str = ''

    if pos_virgula != -1:
        antes_virgula = valor_converter[:pos_virgula]
        depois_virgula = valor_converter[pos_virgula+1:]

        trecho_extra_pos_virgula = 'localizados antes da vírgula, '

    if base_destino == 8:
        numBits = 3
        tabela_temp: list[str] = tabela_binario[:8]
        binario_respectivo: list[str] = [respectivo[1:] for respectivo in tabela_temp]

    if base_destino == 16:
        numBits = 4
        binario_respectivo: list[str] = tabela_binario

    resto_antes = len(antes_virgula) % numBits
    if resto_antes != 0:
        antes_virgula = ((numBits - resto_antes) * '0') + antes_virgula

    resto_depois = len(depois_virgula) % numBits
    if resto_depois != 0:
        depois_virgula = depois_virgula + ((numBits - resto_depois) * '0')

    quantidade_pedacos_antes: int = len(antes_virgula)/numBits
    quantidade_pedacos_depois: int = len(depois_virgula)/numBits
    pulos_trecho: int = numBits
    base_origem: int = 2

    if passos is True:
        print(f"Para converter os valores {trecho_extra_pos_virgula}fazemos o seguinte processo: ")

    valor_convertido_antes_virgula = nucleo_conversao_BHO(
            binario_respectivo, tabela_hexadecimal, quantidade_pedacos_antes,
            pulos_trecho, antes_virgula, base_origem, base_destino, passos
            )

    if pos_virgula != -1:
        if passos is True:
            print("")
            print("~ ---------------------------------------------")
            print("Para os números depois da vírgula fazemos o mesmo processo: ")

        valor_convertido_depois_virgula = nucleo_conversao_BHO(
                binario_respectivo, tabela_hexadecimal, quantidade_pedacos_depois,
                pulos_trecho, depois_virgula, base_origem, base_destino, passos
                )

        return valor_convertido_antes_virgula + "." + valor_convertido_depois_virgula
    else:
        return valor_convertido_antes_virgula


def ho_binario(valor_converter: str, base_origem: int, passos: bool = False) -> str:

    pos_virgula: int = valor_converter.find(".")

    antes_virgula: str = valor_converter
    depois_virgula: str = ''
    trecho_extra_pos_virgula: str = ''

    if pos_virgula != -1:
        antes_virgula = valor_converter[:pos_virgula]
        depois_virgula = valor_converter[pos_virgula + 1:]
        trecho_extra_pos_virgula = 'localizados antes da vírgula, '

    if base_origem == 8:
        tabela_compara: list[str] = tabela_hexadecimal[:8]

        tabela_temp: list[str] = tabela_binario[:8]
        binario_respectivo: list[str] = [respectivo[1:] for respectivo in tabela_temp]

    if base_origem == 16:
        tabela_compara: list[str] = tabela_hexadecimal
        binario_respectivo: list[str] = tabela_binario

    quantidade_pedacos_antes: int = len(antes_virgula)
    quantidade_pedacos_depois: int = len(depois_virgula)
    pulos_trecho: int = 1
    base_destino: int = 2

    if passos is True:
        print(f"Para converter os valores {trecho_extra_pos_virgula}fazemos o seguinte processo: ")

    valor_convertido_antes_virgula: str = nucleo_conversao_BHO(
            tabela_compara, binario_respectivo, quantidade_pedacos_antes,
            pulos_trecho, antes_virgula, base_origem, base_destino, passos
            )
    valor_convertido_depois_virgula: str = ''

    if pos_virgula != -1:
        if passos is True:
            print("")
            print("~ ---------------------------------------------")
            print("Para os números depois da vírgula fazemos o mesmo processo: ")

        valor_convertido_depois_virgula = '.' + nucleo_conversao_BHO(
                tabela_compara, binario_respectivo, quantidade_pedacos_depois,
                pulos_trecho, depois_virgula, base_origem, base_destino, passos,
                True
                )

    return valor_convertido_antes_virgula + valor_convertido_depois_virgula


def ho(valor_converter: str, base_origem: int, base_destino: int, passos: bool = False) -> str:

    if passos is True:
        print(f"Primero convertemos da base {base_origem} para base 2:")

    valor_convertido: str = ho_binario(valor_converter, base_origem, passos)

    if passos is True:
        print("- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Depois convertemos a {valor_convertido}, da base 2, para base {base_destino}")

    valor_convertido = binario_ho(valor_convertido, base_destino, passos)

    return valor_convertido


def nucleo_conversao_BHO(
        tabela_comparacao: list[str], tabela_valor_respectivo: list[str],
        trecho: int, trecho_incrementador: int, valor_converter: str, base_origem: int,
        base_destino: int, passos: bool,
        depois: bool = False
        ) -> str:

    valor_convertido: str = ""

    if passos is True:
        print(f"Olhando da esquerda para a direita agrupamos {trecho_incrementador} caracteres da base {base_origem}, e olhamos o correspondente para esses caracteres na base {base_destino}.")
        print("- ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    for i in range(0, round(trecho)):
        trecho_valor = valor_converter[trecho_incrementador*i : trecho_incrementador + (trecho_incrementador*i)]

        j = tabela_comparacao.index(trecho_valor)
        valor_convertido = valor_convertido + tabela_valor_respectivo[j]

        if passos is True:
            print(f"> '{trecho_valor}' na base {base_origem} -> '{tabela_valor_respectivo[j]}' na base {base_destino}")

    if passos is True:
        print(f"De baixo pra cima, inserindo-os da direita pra esquerda, temos: {valor_convertido}")

    if base_destino == 2:

        inicio: int = 1
        fim: int = len(valor_convertido)
        indice_removedor: int = 0

        if depois is True:
            inicio: int = 0
            fim: int = -1
            indice_removedor: int = -1

        while valor_convertido[indice_removedor] == '0':
            valor_convertido = valor_convertido[inicio:fim]

        if passos is True:
            print(f"Removendo os '0' em excesso ficamos com: {valor_convertido}")

    return valor_convertido


def decimal_universal(valor_converter: str, base_destino: int, passos: bool = False) -> str:

    valor_convertido_antes: str = ''
    valor_convertido_depois: str = ''
    valor_convertido: str = ''

    virgula = valor_converter.find('.')
    antes_virgula = 0
    depois_virgula = 0

    if passos is True:
        print(f"Para converter o valor {valor_converter} fazemos o seguinte processo: ")
        print("~ ---------------------------------------------")

    if virgula != -1:
        antes_virgula = int(valor_converter[:virgula])

        parte_str = valor_converter[virgula+1:]
        depois_virgula = int(parte_str) / (10 ** len(parte_str)) 
        if passos is True:
            print("Primeiro separamos a parte antes e depois da vírgula, para convertermos cada uma delas separadamente: ")
            print("")
            print(f"Parte antes da vírgula: {antes_virgula} | Parte depois da vírgula: {depois_virgula}")
            print("")
            print("Depois convertemos a parte depois da vírgula, multiplicando-a pela base destino \n e pegando a parte inteira do resultado, até que a parte depois da vírgula seja 0 ou tenhamos 16 caracteres: ")
            print(f"Usamos a parte inteira do resultado e verificamos o correspondente na base {base_destino} pela tabela: ") 
            print("")

        while depois_virgula > 0 and len(valor_convertido_depois) <= 16:
            if passos is True:
                print("")
                print(f"  {depois_virgula:.4f} * {base_destino} = {depois_virgula * base_destino:.4f}")
                print("")

            depois_virgula *= base_destino

            numero_virgula = int(depois_virgula)

            if passos is True:
                print(f"  Parte inteira: {numero_virgula} -> '{tabela_hexadecimal[numero_virgula]}' na base {base_destino}")
            valor_convertido_depois += tabela_hexadecimal[numero_virgula]

            depois_virgula -= numero_virgula

        if passos is True:
            print("")
            print(f" A parte depois da vírgula é convertida para: {valor_convertido_depois}")
            print("")
            print("- ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
    else:
        antes_virgula = int(valor_converter)

    if passos is True:

        print("")
        print("Dividimos o número pela base destino, e guardamos o resto, até que o número seja 0: ")
        print(f"Usamos o resto para verificar o correspondente na base {base_destino} pela tabela: ")

    while antes_virgula > 0:

        resto = antes_virgula % base_destino
        if passos is True:
            print("")
            print(f"  {antes_virgula} / {base_destino} = {antes_virgula / base_destino} -> Resto: {resto}")
            print("")
            print(f"  Resto: {resto} -> '{tabela_hexadecimal[resto]}' na base {base_destino}")

        valor_convertido_antes = tabela_hexadecimal[resto] + valor_convertido_antes

        antes_virgula = int(antes_virgula / base_destino)

    if passos is True:
        print("")
        print(f" O número convertido é: {valor_convertido_antes}")
        print("")
        print("- ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("")

    if valor_convertido_depois == '':
        valor_convertido = valor_convertido_antes
    else:
        valor_convertido = valor_convertido_antes + "." + valor_convertido_depois

    return str(valor_convertido)


def universal_decimal(valor_converter: str, base_origem: int, passos: bool = False) -> float:

    virgula = valor_converter.find('.')
    valor_convertido = 0

    if passos is True:
        print(f"Para converter o valor {valor_converter} fazemos o seguinte processo: ")

    if virgula != -1:
        antes_virgula = valor_converter[:virgula]
        depois_virgula = valor_converter[virgula+1:]
        if passos is True:
            print("~ ---------------------------------------------")
            print("Primeiro separamos a parte antes e depois da vírgula, para convertermos cada uma delas separadamente: ")
            print("")
            print(f"Parte antes da vírgula: {antes_virgula} | Parte depois da vírgula: {depois_virgula}")
            print("")
            print("Depois convertemos a parte depois da vírgula, multiplicando cada dígito pelo valor da base elevado a sua posição na tabela, começando do -1: ")
            print("")

        for i, char in enumerate(depois_virgula):

            digito = tabela_hexadecimal.index(char.upper())
            if passos is True:
                print(f"  '{char}' -> {digito} * ({base_origem} ** {-(i + 1)}) = {digito * (base_origem ** -(i + 1))}")
            valor_convertido += digito * (base_origem ** -(i + 1))

        if passos is True:
            print("O resultado da parte depois da vírgula é: " + str(valor_convertido - int(valor_convertido)))
            print("")

    else:
        antes_virgula = valor_converter
        depois_virgula = ''

    if passos is True:
        print("~ ---------------------------------------------")
        print(f"Convertemos {antes_virgula}, multiplicando cada dígito pelo valor da base elevado a sua posição, começando do 0: ")

    for i, char in enumerate(reversed(antes_virgula)):

        digito = tabela_hexadecimal.index(char.upper())
        if passos is True:
            print(f"  '{char}' -> {digito} * ({base_origem} ** {i}) = {digito * (base_origem ** i)}")
        valor_convertido += digito * (base_origem ** i)

    if passos is True:
        print("")
        print(f"O resultado é: {valor_convertido - (valor_convertido - int(valor_convertido))}")

        print("")
        print("~ ---------------------------------------------")
        print("")

    return str(valor_convertido)


def calculadora(nBits: int) -> None:

    max_ = (2 ** nBits) - 1
    max_decimal = str(max_)
    max_binario = decimal_universal(str(max_), 2)
    max_octal = decimal_universal(str(max_), 8)
    max_hexadecimal = decimal_universal(str(max_), 16)

    print(f"Binário: {max_binario}")
    print(f"Decimal: {max_decimal}")
    print(f"Octal: {max_octal}")
    print(f"Hexadecimal: {max_hexadecimal}")
