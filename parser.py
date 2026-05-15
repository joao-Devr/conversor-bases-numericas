def parse_csv():
    import csv
    with open("entrada.csv", "r", newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo, delimiter=";")
 
        for linha in leitor:
            valor        = linha["valor"]
            base_origem  = linha["base_origem"]
            base_destino = linha["base_destino"]
 
            print(f"Valor: {valor} | Base origem: {base_origem} | Base destino: {base_destino}")   
        arquivo.close()