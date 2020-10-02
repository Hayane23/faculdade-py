# calculo.py

import figuras

def calculo():
    raio = 0
    pergunta = input('Gostaria de informar o valor do raio? Dirgite S para sim: ')

    if pergunta == 'S' or pergunta == 's':
        raio = float(input('Informe o valor do Raio: '))
    else:
        raio = 2
    
    print(figuras.calculo_perimetro(raio))

calculo()
