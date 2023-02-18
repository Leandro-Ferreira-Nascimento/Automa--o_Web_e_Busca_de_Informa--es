
# Passo 4: Atualizar a base de preços (atualizando o preço de compra e o valor de venda)

import pandas as pd
tabela= pd.read_excel('Produtos.xlsx')
display(tabela)

### Atualizando os preços e o cáculo do preço final 

# OBS: Como todas essas informações vieram de um texto de um site as 
#      informações tambem são um texto(str)


# Atualizando a coluna de cotação( Quero editar a coluna cotação, onde a coluna moeda = Dólar)
# tabela.loc[linha, coluna]
# localizei a linha e coluna, no pandas consigo fazer todas as linhas e colunas de uma vez
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)   
# Estou comparando qdo Moeda for igual a Dolar, vou querer editar a coluna cotação para um float 


tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)   
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)  

# Atualizar a coluna de preço de compra = preço original * cotação
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']
# A coluna preço de comprar da tabela vai ser igual a multiplicação da coluna Preço Original * Cotação

# Atualizar a coluna de preço de venda = preço de compra * margem 
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

display (tabela)