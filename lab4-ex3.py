print('========== exercício 3 ==========')
print('Preço por tipo de e faixa de consumo eletrico')
tipo_instalacao = str(input('Insira o tipo de de isntalassão, sendo R para (Residencial); C para (Comercial); I para (Industrial): '))
consumo_kwh = int(input('Qual foi o consume em kWh? '))

if tipo_instalacao == 'R' or 'r' and consumo_kwh <= 500:
    preco = consumo_kwh * 0.40
    print('Consumo R$:', preco)
elif tipo_instalacao == 'R' or 'r' and consumo_kwh > 500:
    preco = consumo_kwh * 0.65
    print('Consumo R$:', preco)
elif tipo_instalacao == (('C' or 'c') and ('I' or 'i')) and consumo_kwh <= 500:
    preco = consumo_kwh * 0.55
    print('Consumo R$:', preco)
elif tipo_instalacao == (('C' or 'c') and ('I' or 'i')) and consumo_kwh > 500:
    preco = consumo_kwh * 0.60
    print('Consumo R$:', preco)
else:
    print('Valor invalido')