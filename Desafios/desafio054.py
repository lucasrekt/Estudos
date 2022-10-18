# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são de maiores.

from datetime import date

# cont = 0
# hoje = date.today().year
# for c in range(1, 8):
#     ano = int(input('Qual o seu ano de nascimento? '))
#     if (ano - hoje) < 18:
#         cont += 1
#         print('Desse grupo, {} pessoas são de menor'.format(cont), end='')
#     else:
#         cont += 1
#         print(', e {} pessoas são de maior.'.format(cont))

atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
