# pegar o número de dias, multiplicar por 3, multiplicar por 60, multiplicar por 24000, dividir por 20, depois dividir por 2, pois ele só constrói durante a manhã e por fim, divide pelo número de casas

dias = int(input())
casas = int(input())

ticks = (((dias * 3 * 60 *24000) / 20) / 2) / casas

print(f'{ticks:.0f}')