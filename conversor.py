simbolos_permitidos = [
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
    for simbolo_inserido in valor:
        existe_simbolo: bool = False

        for i in range(0, base_origem):
            if simbolo_inserido == simbolos_permitidos[i]:
                existe_simbolo = True
        
        if existe_simbolo == False:
            print(f"O simbolo '{simbolo_inserido}' não pertence a base {base_origem} \n")
            return False

    return True
   
def conversao_binario_hexa(valor: str, base_origem:int):
    if base_origem == 2:
        binario_hexa(valor)

def binario_hexa(valor: str) -> None:
    resposta: str = ""
    
    resto = len(valor) % 4
    if resto != 0:
        valor = ((4 - resto) * '0') + valor
    
    for i in range(0, round(len(valor)/4)):
        trecho_valor = valor[4*i : 4+ (4*i)]

        for j in range(0, len(tabela_binario)):
            
            if trecho_valor == tabela_binario[j]:
                resposta = resposta + simbolos_permitidos[j]

    print(resposta)



conversao_binario_hexa('1001011110', 2)


