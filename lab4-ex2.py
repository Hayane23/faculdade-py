print('========== exercício 2 ==========')
a = float(input('Insira o valor do primeiro A do triangulo: '))
b = float(input('Insira o valor do primeiro B do triangulo: '))
c = float(input('Insira o valor do primeiro C do triangulo: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print ('Não é possível formar um triangulo.')
elif (a == b) and (b == c):
    print('É um triângulo equilátero')
elif (a == b) or (b == c) or (c == a):
    print('É um triângulo isósceles')
elif (a != b) and (b != c) and (c != a):
    print('É um triângulo escaleno')
