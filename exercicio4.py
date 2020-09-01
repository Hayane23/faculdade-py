print('======== exercicio 04 =======')
print('Vamos caucular o seu Indice de Massa Corporal (IMC)')
peso = float(input('Qual o seu peso atualmente? '))
altura = float(input('E qual a sua altura? '))
imc = peso / (altura * altura)
if imc < 17:
    print('debug 1')
    print('Seu IC atual é de: ', imc, 'Você está muito abaixo do peso.')
elif imc >= 17 and imc < 18.50:
    print('debug 2')
    print('Seu IMC atual é de: ', imc, 'Você está abaixo do peso.')
elif imc >= 18.50 and imc < 24.99:
    print('Seu IMC atual é de: ', imc, 'Você está em seu peso normal.')
elif imc >= 24.99 and imc < 30:
    print('Seu IMC atual é de: ', imc, 'Você está acima do peso.')
elif imc >= 30 and imc < 35:
    print('Seu IMC atual é de: ', imc, 'Você está com obesidade I.')
elif imc >= 35 and imc < 40:
    print('Seu IMC atual é de: ', imc, 'Você está com obesidade II.')
else:
    print('Seu IMC é: ', imc, 'Você está com obesidade III.' )
