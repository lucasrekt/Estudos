frase = 'Curso em Vídeo Python'
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print('-' * 20)

len(frase)
print(len(frase))

print('-' * 20)

frase.count('o')
print(frase.count('o, 0 , 13'))  # fatiamento com count, do caractere 0 ao 13.

print('-' * 20)

frase.find('deo')
print(frase.find('deo'))  # encontra onde começa algo com "deo".
print(frase.find('Android'))  # não existe, então retorna -1
print('Curso' in frase)

print('-' * 20)

# Transformação

frase.replace('Python', 'Android')  # Realoca tudo que estiver "Python" para "Android"
frase.upper()  # Deixa tudo em maiusculo.
frase.lower()  # Deixa tudo em minúsculo.
frase.capitalize()  # Só deixa o primeiro caractere em maiúsculo.
frase.title()  # Deixa todos os primeiros caracteres das palavras em maiúsculo.
print(frase.replace('Python', 'Android'))
frase2 = '   Aprenda Python  '
frase2.strip()  # Remove todos os espaços inúteis da string, sendo os inicias e finais.
frase2.rstrip()  # Remove apenas os espaços da direita.
frase2.lstrip()  # Remove apenas os espaços da esquerda.

# Divisão

frase.split()  # Faz com que cada palavra de uma string, recomece sua contagem de espaços.
# Gera uma lista para cada palavra.

# Junção

'-'.join(frase)
print(frase)
