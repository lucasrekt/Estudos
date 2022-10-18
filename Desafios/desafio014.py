# Converta uma temperatura digitando em graus Cº e converta pra Fahrenheit.

c = float(input('Informe a temperatura em Cº:'))
f = c * 1.8 + 32
# f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
