tamanho = int(input('Qual o tamanho da área a ser pintada em metros: '))
lata_de_tinta = tamanho//18
if tamanho//18 < tamanho/18:
    valor_da_lata_de_tinta = 80 * (lata_de_tinta+1)
    print(f'Você irá comprar {lata_de_tinta+1} lata(s) de tinta e custará R${valor_da_lata_de_tinta}.')
else:
    valor_da_lata_de_tinta = 80 * lata_de_tinta
    print(f'Você irá comprar {lata_de_tinta} lata(s) de tinta e custará R${valor_da_lata_de_tinta}.')
