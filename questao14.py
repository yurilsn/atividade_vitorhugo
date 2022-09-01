peso = float(input('Digite o peso do peixe: '))

if peso > 50:
    excesso = peso - 50
    multa = excesso*4
    print(f'O peixe pesou {excesso}Kg acima do permitido.')
    print(f'O valor da multa a ser pago é de R${multa:.2f}.')
else:
    print('O peso peixe está de acordo com o regulamento.')
