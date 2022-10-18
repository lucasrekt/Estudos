# Leia o nome, idade e sexo de 4 pessoas. Mostre a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

soma = 0
velho = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('-' * 20, '{}ª PESSOA'.format(c), '-' * 20)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma += idade
    if c == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print('A média de idade do grupo é de {} anos'.format(soma / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

