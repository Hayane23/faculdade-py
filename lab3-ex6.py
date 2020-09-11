print('========== exercicio 6 ==========')
print('Vamos escolher um numero.')
numero = int(input('Inrira um número do tipo inteiro:'))

if numero < 0: 
    print('O número não pode ser negativo.')
elif numero == 0:
    print('Zero?!?')
elif numero == 1:
    print('Um é pouco!')
elif numero == 2:
    print('Dois é bom!')
else:
    print('É demais!')