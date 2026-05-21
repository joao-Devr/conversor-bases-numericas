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
    simbolos_permitidos = tabela_hexadecimal

    for simbolo_inserido in valor:
        existe_simbolo: bool = False

        for i in range(0, base_origem):
            if simbolo_inserido == simbolos_permitidos[i]:
                existe_simbolo = True
        
        if existe_simbolo == False:
            print(f"O simbolo '{simbolo_inserido}' não pertence a base {base_origem} \n")
            return False

    return True

def binario_ho(valor: str, base_destino: int) -> str:
    
    if base_destino == 8:
        numBits = 3
        tabela_temp = tabela_binario[:8]
        tabela_respectivo = [respectivo[1:] for respectivo in tabela_temp]

    if base_destino == 16:
        numBits = 4
        tabela_respectivo = tabela_binario

    resto = len(valor) % numBits
    if resto != 0:
        valor = ((numBits - resto) * '0') + valor

    quantidade_pedacos: int = len(valor)/numBits
    complemento_pulos_trecho: int = numBits
    pulos_trecho: int = numBits
    base_origem: int = 2

   
    return nucleo_conversao_BHO(tabela_respectivo, tabela_hexadecimal, quantidade_pedacos, pulos_trecho, complemento_pulos_trecho, valor, base_origem)

def ho_binario(valor:str, base_origem: int) -> str:
    
    if base_origem == 8:
        tabela_compara = tabela_hexadecimal[:8]

        tabela_temp = tabela_binario[:8]
        tabela_respectivo = [respectivo[1:] for respectivo in tabela_temp]


    if base_origem == 16:
        tabela_compara = tabela_hexadecimal
        tabela_respectivo = tabela_binario

    quantidade_pedacos: int = len(valor)
    pulos_trecho: int = 1
    complemento_pulos_trecho: int = 1

    return nucleo_conversao_BHO(tabela_compara, tabela_respectivo, quantidade_pedacos, pulos_trecho, complemento_pulos_trecho, valor, base_origem)

def ho(valor:str, base_origem: int, base_destino:int) -> str:
    resposta = ho_binario(valor, base_origem)
    resposta = binario_ho(resposta, base_destino)
    return resposta

def nucleo_conversao_BHO(tabela_comparacao, tabela_valor_respectivo, trecho: int, multiplicador_trecho: int, soma_trecho:int, valor:str, base_origem: int):
    resposta: str = ""

    for i in range(0, round(trecho)):
        trecho_valor = valor[multiplicador_trecho*i : soma_trecho + (multiplicador_trecho*i)]
            
        for j in range(0, len(tabela_comparacao)):
                 
            if trecho_valor == tabela_comparacao[j]:
                resposta = resposta + tabela_valor_respectivo[j]

    if base_origem == 16 or base_origem == 8:
        while(resposta[0] == '0'):
            resposta = resposta[1:]

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

print(binario_ho("1011", 16))
