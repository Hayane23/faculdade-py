print('========== exercício 1 ==========')

def calcular_media():
    nota_1 = float(input('Insira o valor da primeira nota: '))
    nota_2 = float(input('Insira o valor da Segunda nota: '))
    nota_3 = float(input('Insira o valor da terceira nota: '))
    nota_4 = float(input('Insira o valor da quarta nota: '))
    calculo = (nota_1 + nota_2 + nota_3 + nota_4)/4
    aredondar = round(calculo,2)
    return aredondar

media = calcular_media()

def status_media():
    if media < 4:
        print('Sua media é', media, 'Você está reprovado.')
    elif media >= 4 and media <= 6 :
        print('Sua media é', media, 'Você está de exame.')
    else:
        print('Sua media é', media, 'Você está aprovado.')

print('Calculo da Media')
print('=================')
status_media()
print('=================')