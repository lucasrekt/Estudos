# Par ou Impar

from random import randint

print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)
c = 0

while True:
    n = int(input('Diga um valor: '))
    p = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(1, 10)
    soma = n + computador
    conta = soma % 2
    if conta == 0:
        resultado = 'DEU PAR'
    else:
        resultado = 'DEU IMPAR'
    print(f'Você jogou {n} e o computador {computador}. Total de {soma} {resultado}')
    if p == 'P' and conta == 0:
        print('Você VENCEU!\n'
              'Vamos jogar novamente...')
        c += 1
        print('=-' * 30)
    else:
        print('Você PERDEU!\n')
        print('=-' * 30)
        break
print(f'GAME OVER! Você venceu {c} vezes.')
