tabela_hexadecimal = [
        '0', '1', '2', '3', '4', '5', 
        '6', '7', '8', '9', 'A', 'B', 
        'C', 'D', 'E', 'F'
        ]
tabela_binario = [
        '0000', '0001', '0010', '0011', '0100', 
        '0101', '0110', '0111', '1000', '1001', 
        '1010', '1011', '1100', '1101', '1110', '1111'
        ]


def validar_valor(valor: str, base_origem:int) -> bool:
    simbolos_permitidos = tabela_hexadecimal[:base_origem]
    simbolos_permitidos.append('.')

    for simbolo_inserido in valor:
        existe_simbolo: bool = False

        if simbolo_inserido in simbolos_permitidos:
            existe_simbolo = True

        if existe_simbolo == False:
            print(f"O simbolo '{simbolo_inserido}' não pertence a base {base_origem} \n")
            return False

    return True

def binario_ho(valor: str, base_destino: int, passos: bool = False) -> str:

    pos_virgula: int = valor.find('.')

    antes_virgula: str = valor
    depois_virgula: str = ''
    trecho_extra_pos_virgula: str = ''

    if pos_virgula != -1:
        antes_virgula = valor[:pos_virgula]
        depois_virgula = valor[pos_virgula+1:]

        trecho_extra_pos_virgula = 'localizados antes da vírgula, '


    if base_destino == 8:
        numBits = 3
        tabela_temp = tabela_binario[:8]
        tabela_respectivo = [respectivo[1:] for respectivo in tabela_temp]

    if base_destino == 16:
        numBits = 4
        tabela_respectivo = tabela_binario

    resto_antes = len(antes_virgula) % numBits
    
    if resto_antes != 0:
        antes_virgula = ((numBits - resto_antes) * '0') + antes_virgula

    resto_depois = len(depois_virgula) % numBits
    if resto_depois != 0:
        depois_virgula = depois_virgula + ((numBits - resto_depois) * '0')

    quantidade_pedacos_antes: int = len(antes_virgula)/numBits
    quantidade_pedacos_depois: int = len(depois_virgula)/numBits
    complemento_pulos_trecho: int = numBits
    pulos_trecho: int = numBits
    base_origem: int = 2

    if passos == True:
        print(f"Para converter os valores {trecho_extra_pos_virgula}fazemos o seguinte processo: ")
    resposta_antes_virgula = nucleo_conversao_BHO(tabela_respectivo, tabela_hexadecimal, quantidade_pedacos_antes, pulos_trecho, complemento_pulos_trecho, antes_virgula, base_origem, base_destino, passos)

    if pos_virgula != -1:
        if passos == True:
            print("")
            print("~ ---------------------------------------------")
            print("Para os números depois da vírgula fazemos o mesmo processo: ")
        resposta_depois_virgula = nucleo_conversao_BHO(tabela_respectivo, tabela_hexadecimal, quantidade_pedacos_depois, pulos_trecho, complemento_pulos_trecho, depois_virgula, base_origem, base_destino, passos)

        return resposta_antes_virgula + "." + resposta_depois_virgula
    else:
        return resposta_antes_virgula

def ho_binario(valor:str, base_origem: int, passos: bool = False) -> str:

    antes_virgula = valor
    depois_virgula = ''
    trecho_extra_pos_virgula: str = ''

    pos_virgula = valor.find(".")

    if pos_virgula != -1:
        antes_virgula = valor[:pos_virgula]
        depois_virgula = valor[pos_virgula + 1:]
        trecho_extra_pos_virgula = 'localizados antes da vírgula, '
    
    if base_origem == 8:
        tabela_compara = tabela_hexadecimal[:8]

        tabela_temp = tabela_binario[:8]
        tabela_respectivo = [respectivo[1:] for respectivo in tabela_temp]


    if base_origem == 16:
        tabela_compara = tabela_hexadecimal
        tabela_respectivo = tabela_binario

    quantidade_pedacos_antes: int = len(antes_virgula)
    quantidade_pedacos_depois: int = len(depois_virgula)
    pulos_trecho: int = 1
    complemento_pulos_trecho: int = 1
    base_destino: int = 2 

    if passos == True:
        print(f"Para converter os valores {trecho_extra_pos_virgula}fazemos o seguinte processo: ")
    resposta_antes_virgula = nucleo_conversao_BHO(tabela_compara, tabela_respectivo, quantidade_pedacos_antes, pulos_trecho, complemento_pulos_trecho, antes_virgula, base_origem, base_destino, passos)

    if pos_virgula != -1:
        if passos == True:
            print("")
            print("~ ---------------------------------------------")
            print("Para os números depois da vírgula fazemos o mesmo processo: ")
         
        resposta_depois_virgula = nucleo_conversao_BHO(tabela_compara, tabela_respectivo, quantidade_pedacos_depois, pulos_trecho, complemento_pulos_trecho, depois_virgula, base_origem, base_destino, passos, True)

        return resposta_antes_virgula + "." + resposta_depois_virgula

    else:
        return resposta_antes_virgula
 


def ho(valor:str, base_origem: int, base_destino:int, passos: bool = False) -> str:
    if passos == True:
        print(f"Primero convertemos da base {base_origem} para base 2:")
    resposta = ho_binario(valor, base_origem, passos)
    if passos == True:
        print("- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Depois convertemos a {resposta}, da base 2, para base {base_destino}")
    resposta = binario_ho(resposta, base_destino, passos)
    return resposta

def nucleo_conversao_BHO(tabela_comparacao, tabela_valor_respectivo, trecho: int, multiplicador_trecho: int, soma_trecho:int, valor:str, base_origem: int, base_destino: int, passos: bool, depois: bool = False):
    resposta: str = ""
    
    if passos == True:
        print(f"Olhando da esquerda para a direita agrupamos {soma_trecho} caracteres da base {base_origem}, e olhamos o correspondente para esses caracteres na base {base_destino}.")
        print("- ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    for i in range(0, round(trecho)):
        trecho_valor = valor[multiplicador_trecho*i : soma_trecho + (multiplicador_trecho*i)]
            
        j = tabela_comparacao.index(trecho_valor)
        resposta = resposta + tabela_valor_respectivo[j]
        
        if passos == True:
            print(f"> '{trecho_valor}' na base {base_origem} -> '{tabela_valor_respectivo[j]}' na base {base_destino}")

    if passos == True:
        print(f"De baixo pra cima, inserindo-os da direita pra esquerda, temos: {resposta}")


    if base_destino == 2:
        if depois == False:
            while(resposta[0] == '0'):
                resposta = resposta[1:]
        
        if depois == True:
            while(resposta[-1] == '0'):
                resposta = resposta[:-1]

        if passos == True:
            print(f"Removendo os '0' em excesso ficamos com: {resposta}")

    return resposta



def decimal_universal(valor: str, base_destino: int, passos: bool = False) -> str:
        
        resposta_antes = ''
        resposta_depois = ''
        resposta = ''

        virgula = valor.find('.')
        antes_virgula = 0
        depois_virgula = 0

        if passos == True:
            print(f"Para converter o valor {valor} fazemos o seguinte processo: ")
            print("~ ---------------------------------------------")

        if virgula != -1:
         antes_virgula = int(valor[:virgula])

         parte_str = valor[virgula+1:]
         depois_virgula = int(parte_str) / (10 ** len(parte_str)) 
         if passos == True:
            print(f"Primeiro convertemos a parte depois da vírgula, multiplicando-a pela base destino \n e pegando a parte inteira do resultado, até que a parte depois da vírgula seja 0 ou tenhamos 16 caracteres: ")
         while depois_virgula > 0 and len(resposta_depois) <= 16:
        
                depois_virgula *= base_destino
    
                numero_virgula = int(depois_virgula)
    
                resposta_depois += tabela_hexadecimal[numero_virgula]

                depois_virgula -= numero_virgula

         if passos == True:
             print("")
             print(f" A parte depois da vírgula é convertida para: {resposta_depois}")
             print("")
             print("- ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        else:
            antes_virgula = int(valor)


        if passos == True:
           
            print("")
            print(f"Dividimos o número pela base destino, e guardamos o resto, até que o número seja 0: ")

        while antes_virgula > 0:
         
         resto = antes_virgula % base_destino
         if passos == True:
            print(f"  {antes_virgula} / {base_destino} = {antes_virgula / base_destino} -> Resto: {resto}")
        
         resposta_antes = tabela_hexadecimal[resto] + resposta_antes


         antes_virgula = int(antes_virgula / base_destino)
    
        if passos == True:
            print("")
            print(f" O número convertido é: {resposta_antes}")
            print("")
            print("- ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
            print("")

        if resposta_depois == '':
            resposta = resposta_antes
        else:
             resposta = resposta_antes + "." + resposta_depois

        return str(resposta)

def universal_decimal(valor: str, base_origem: int, passos: bool = False) -> float:

    virgula = valor.find('.')
    resultado = 0

    if passos == True:
            print(f"Para converter o valor {valor} fazemos o seguinte processo: ")
            
       
    if virgula != -1:
        antes_virgula = valor[:virgula]
        depois_virgula = valor[virgula+1:]
        if passos == True:
         print("~ ---------------------------------------------")
         print(f"Primeiro separamos a parte antes e depois da vírgula, para convertermos cada uma delas separadamente: ")
         print("")
         print(f"Parte antes da vírgula: {antes_virgula} | Parte depois da vírgula: {depois_virgula}")
         print("")  
         print(f"Depois convertemos a parte depois da vírgula, multiplicando cada dígito pelo valor da base elevado a sua posição, começando do -1: ")
         print("")
        for i, char in enumerate(depois_virgula):

         digito = tabela_hexadecimal.index(char.upper())

         resultado += digito * (base_origem ** -(i + 1))

        if passos == True:
         print("O resultado da parte depois da vírgula é: " + str(resultado - int(resultado)))
         print("")      
        
    else:

        antes_virgula = valor
        depois_virgula = ''

  
    for i, char in enumerate(reversed(antes_virgula)):

        digito = tabela_hexadecimal.index(char.upper())

        resultado += digito * (base_origem ** i)

    if passos == True:
         print("~ ---------------------------------------------")
         print(f"Convertemos {antes_virgula}, multiplicando cada dígito pelo valor da base elevado a sua posição, começando do 0: ")
         print("")
         print(f"O resultado é: {resultado - (resultado - int(resultado))}")
    
         print("")
         print(f"~ ---------------------------------------------")
         print("")
         
    return str(resultado)


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
