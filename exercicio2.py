print('======== exercício 02 =======')
print('Vamos calcular a quilometragem e consumo de combustível de um veículo.')
tempo = int(input('Insira o tempo médio em horas percorridas: '))
velocidade = int(input('Insira a velocidade media do trajeto: '))
distancia = tempo * velocidade
print ('A distância percorrida foi de: ', distancia , 'km')
consumo = distancia/12
print ('O consumo de combustível foi: ', consumo, 'L')