# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
# salário, com 15% de aumento.
si = float(input('Qual o seu salário?'))
a = si * (15 / 100)
sf = si + a
print('Com o aumento de 15% seu salário vai para: R${:.2f}'.format(sf))
