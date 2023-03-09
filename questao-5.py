def inverteString():
    stringOriginal = input("Informe a string a ser invertida: ")
    stringInvertida = stringOriginal[::-1] #utilizando a técnica do slice
    print(stringInvertida)

inverteString()