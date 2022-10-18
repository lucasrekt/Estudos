# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date

atual = date.today().year
nasc = int(input('Qual seu ano de nascimento?'))
idade = atual - nasc
print('A idade do atleta é {} anos.'.format(idade))

if idade <= 9:
    print('Sua categoria na competição é Mirim!')
elif idade <= 14:
    print('Sua categoria na competição é Infantil!')
elif idade <= 19:
    print('Sua categoria na competição é Júnior!')
elif idade <= 25:
    print('Sua categoria na competição é Sênior!')
else:
    print('Sua categoria na competição é Master!')
