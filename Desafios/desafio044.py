# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('============Lojas TFT============')
preco = float(input('Preço da compras: R$'))
# op = int(input('FORMAS DE PAGAMENTO\n'
#                '[ 1 ] à vista dinheiro/cheque\n'
#                '[ 2 ] à vista cartão\n'
#                '[ 3 ] 2x no cartão\n'
#                '[ 4 ] 3x ou mais no cartão\n'
#                'Qual é a opção de pagamento? '))
while True:
    op = int(input('FORMAS DE PAGAMENTO\n'
                   '[ 1 ] à vista dinheiro/cheque\n'
                   '[ 2 ] à vista cartão\n'
                   '[ 3 ] 2x no cartão\n'
                   '[ 4 ] 3x ou mais no cartão\n'
                   'Qual é a opção de pagamento? '))
    if op == 1:
        desc = preco - (preco * 0.10)
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desc))
    elif op == 2:
        desc = preco - (preco * 0.05)
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desc))
    elif op == 3:
        print('Sua compra ficou R${:.2f}.'.format(preco))
    elif op == 4:
        juros = preco + (preco * 0.20)
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, juros))
    else:
        print('Opção incorreta, tente novamente!')
        continue
    break
print('Encerrando o pagamento.')
