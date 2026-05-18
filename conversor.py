simbolos_permitidos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

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
    


