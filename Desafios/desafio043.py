# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu ÍMC e mostre seu status:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = int(input('Qual o seu peso? (Kg) '))
h = float(input('Qual a sua altura? (m) '))
imc = peso / h**2
print('Seu IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no Peso Ideal')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso')
elif 30 <= imc < 40:
    print('Você está em Obesidade')
else:
    print('Você está em Obesidade Mórbida')
