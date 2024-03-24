def inverter_string():
    while True:
        string_original = input("\n Digite uma string para inverter (ou digite 'sair' para encerrar): ")
        
        if string_original.lower() == "sair":
            print("\n Programa encerrado.\n ")
            break
        
        string_invertida = ""
        
        i = len(string_original) - 1
        while i >= 0:
            string_invertida += string_original[i]
            i -= 1
        
        print("\n Palavra original:", string_original)
        print("\n Palavra invertida:", string_invertida)

inverter_string()

