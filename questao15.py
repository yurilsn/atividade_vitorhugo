valor_hora = float(input('Quanto você ganha por hora trabalhada: '))
hora_trabalhada = float(input('Quantas horas você trabalhou neste mês: '))
salario_bruto = valor_hora*hora_trabalhada
imposto_de_renda = 11/100*salario_bruto
INSS = 8/100*salario_bruto
sindicato = 5/100*salario_bruto
salario_liquido = salario_bruto - imposto_de_renda - INSS - sindicato

print(f'+ Salário Bruto : R${salario_bruto}')
print(f'- IR (11%) : R${imposto_de_renda}')
print(f'- INSS (8%) : R${INSS}')
print(f'- Sindicato ( 5%) : R${sindicato}')
print(f'= Salário Liquido : R${salario_liquido}')

