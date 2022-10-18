# Crie um programa que leia vários números pelo teclado. No final, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos.

# c = 0
# num = 0
# q = 0
#
# while q != 'N':
#     c += 1
#     num = int(input('Digite um número: '))
#     q = str(input('Quer continuar [S/N]')).strip().upper()
# print('Você digitou {} números e a média foi {}'.format(c, num))

resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
