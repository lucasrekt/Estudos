# Refaça o Desafio 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Digite o número que deseja ver a tabuada: '))
for n in range(1, 11):
    print('{} x {} = {}'.format(num, n, num * n))
