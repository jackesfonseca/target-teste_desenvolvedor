def calculaPercentual():

    SP = 67836.43
    RJ = 36678.66
    MG = 29229.88
    ES = 27165.48
    outros = 19849.53

    total = SP + RJ + MG + ES + outros

    print("SP: ", (100*SP)/total, "%")
    print("RJ: ", (100*RJ)/total, "%")
    print("MG: ", (100*MG)/total, "%")
    print("ES: ", (100*ES)/total, "%")
    print("outros: ", (100*outros)/total, "%")

calculaPercentual()