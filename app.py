import meumodulo as mm


valores = [18, 34, 28, 45, 17, 99, 40]

cv = mm.coeficiente_de_variação(valores)
print(f'O coeficiente de variação {cv:.3f}')

med = mm.mediana(valores)
print(f'A mediana dos dados é: {med}')

std = mm.standard_deviation(valores)
print(f'O desvio padrão dos dados é: {std:.3f}')