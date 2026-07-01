import statistics as stts

def variancia (dados):
    Valeus = stts.variance(dados)
    return(dados)

def standard_deviation (dados):
    values = stts.stdev(dados)
    return values

def mediana (dados):
    values = stts.median(dados)
    return values

def coeficiente_de_variação (dados):
    values = stts.mean(dados)
    Valor = stts.stdev(dados)
    cv = (Valor/values)*100
    return cv
    
def mean (dados):
    média = stts.mean(dados)
    return (dados)