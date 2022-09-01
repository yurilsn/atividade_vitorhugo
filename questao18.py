tamanho_do_arquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade_da_internet = float(input('Digite a velocidade da internet Mbps: '))

tempo_de_download = tamanho_do_arquivo/(velocidade_da_internet/8)
print(f'O tempo de download desse arquivo é de {tempo_de_download/60:.2f} minutos.')