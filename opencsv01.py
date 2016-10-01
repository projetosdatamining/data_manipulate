filename = '/home/data/dados.csv'
with open(filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    meus_dados = list(reader)
    
#mostra linha de cabecalhos
print(meus_dados[0])
#mostra dados da primeira linha
print(meus_dados[1])
