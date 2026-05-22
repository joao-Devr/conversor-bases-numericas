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

def binario_ho(valor: str, base_destino: int) -> str:

    pos_virgula = valor.find('.')

    antes_virgula = valor
    depois_virgula = ''

    if pos_virgula != -1:
        antes_virgula = valor[:pos_virgula]
        depois_virgula = valor[pos_virgula+1:]

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

    resposta_antes_virgula = nucleo_conversao_BHO(tabela_respectivo, tabela_hexadecimal, quantidade_pedacos_antes, pulos_trecho, complemento_pulos_trecho, antes_virgula, base_origem)

    if pos_virgula != -1: 
        resposta_depois_virgula = nucleo_conversao_BHO(tabela_respectivo, tabela_hexadecimal, quantidade_pedacos_depois, pulos_trecho, complemento_pulos_trecho, depois_virgula, base_origem)

        return resposta_antes_virgula + "." + resposta_depois_virgula
    else:
        return resposta_antes_virgula

def ho_binario(valor:str, base_origem: int) -> str:

    antes_virgula = valor
    depois_virgula = ''

    pos_virgula = valor.find(".")

    if pos_virgula != -1:
        antes_virgula = valor[:pos_virgula]
        depois_virgula = valor[pos_virgula + 1:]
    
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

    resposta_antes_virgula = nucleo_conversao_BHO(tabela_compara, tabela_respectivo, quantidade_pedacos_antes, pulos_trecho, complemento_pulos_trecho, antes_virgula, base_origem)

    if pos_virgula != -1:
        resposta_depois_virgula = nucleo_conversao_BHO(tabela_compara, tabela_respectivo, quantidade_pedacos_depois, pulos_trecho, complemento_pulos_trecho, depois_virgula, base_origem, True)

        return resposta_antes_virgula + "." + resposta_depois_virgula

    else:
        return resposta_antes_virgula
 


def ho(valor:str, base_origem: int, base_destino:int) -> str:
    resposta = ho_binario(valor, base_origem)
    resposta = binario_ho(resposta, base_destino)
    return resposta

def nucleo_conversao_BHO(tabela_comparacao, tabela_valor_respectivo, trecho: int, multiplicador_trecho: int, soma_trecho:int, valor:str, base_origem: int, depois: bool = False):
    resposta: str = ""

    for i in range(0, round(trecho)):
        trecho_valor = valor[multiplicador_trecho*i : soma_trecho + (multiplicador_trecho*i)]
            
        j = tabela_comparacao.index(trecho_valor)
        resposta = resposta + tabela_valor_respectivo[j]

    if base_origem == 16 or base_origem == 8:
        if depois == False:
            while(resposta[0] == '0'):
                resposta = resposta[1:]
        
        if depois == True:
            while(resposta[-1] == '0'):
                resposta = resposta[:-1]

    return resposta



def decimal_universal(valor: str, base_destino: int) -> str:
   
    resposta = ''
    valor = int(valor)

    while valor > 0:
         
         resto = valor % base_destino

         resposta = tabela_hexadecimal[resto] + resposta

         valor = int(valor / base_destino)

    return resposta

def universal_decimal(valor: str, base_origem: int) -> int:
    
    i = 0
    resultado = 0
    
    for char in reversed(valor):

        valor = tabela_hexadecimal.index(char)

        resultado += valor * (base_origem ** i)

        i += 1
        
    return resultado

