tamanho = int(input('Qual o tamanho da área a ser pintada em metros: '))/6


lata_de_tinta = tamanho//18
if tamanho//18 < tamanho/18:
    valor_da_tinta = 80 * (lata_de_tinta+1)
    print(f'\n--Se comprar {lata_de_tinta+1} lata(s) de 18L de tinta, custará R${valor_da_tinta}.')
else:
    valor_da_tinta = 80 * lata_de_tinta
    print(f'\n--Se comprar {lata_de_tinta} lata(s) de 18L de tinta, custará R${valor_da_tinta}.')


lata_de_tinta_2 = tamanho//3.6
if tamanho//3.6 < tamanho/3.6:
    valor_da_tinta = 25 * (lata_de_tinta_2+1)
    print(f'\n--Se comprar {lata_de_tinta_2+1} galões de 3.6L de tinta, custará R${valor_da_tinta}.')
else:
    valor_da_tinta = 25 * lata_de_tinta_2
    print(f'\n--Se comprar {lata_de_tinta_2} galões de 3.6L de tinta, custará R${valor_da_tinta}.')


lata_de_tinta = tamanho//18
if tamanho//18 < tamanho/18:
    valor_da_tinta = 80 * (lata_de_tinta+1)
else:
    valor_da_tinta = 80 * lata_de_tinta
valor_da_tinta = lata_de_tinta*80
resto_da_tinta = tamanho%18
lata_de_tinta_2  = resto_da_tinta//3.6
if resto_da_tinta != 0:
    if resto_da_tinta//3.6 < resto_da_tinta/3.6:  
        valor_da_tinta_2 = 25*(lata_de_tinta_2 + 1)
        total = valor_da_tinta + valor_da_tinta_2
        print(f'\n--Comprando {lata_de_tinta} lata(s) de 18L e {lata_de_tinta_2+1} galões de 3.6L custará R${total}.')
    else:
        valor_da_tinta_2 = 25*lata_de_tinta_2
        print(f'\n--Comprando {lata_de_tinta} lata(s) de 18L e {lata_de_tinta_2} galões de 3.6L custará R${total}.')
else:
    print(f'\n--Comprando gastos {lata_de_tinta} lata(s) de tinta de 18L e custará R${valor_da_tinta}.')

#observação: não consegui tirar os 10%.
