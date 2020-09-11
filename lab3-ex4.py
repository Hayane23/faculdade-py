print('======== exercicio 04 =======')
c_direita = float(input('Qual a temperatura da ponta direita da barra? '))
c_esquerda = float(input('Qual a temperatura da ponta esquerda da barra? '))
temperaturas = (c_direita + c_esquerda) / 2
media = round(temperaturas,2)
if media <= 35:
    print('A temperatura no centro da barra é: ', media, 'pode pegar.')
else:
    print('A temperatura no centro da barra é: ', media, 'Cuidado! A barra está quente')
