
# Instalando a Biblioteca 
!pip install selenium

# Importado as bibliotecas que vou usar.
from selenium import webdriver # permite criar o navegador
from selenium.webdriver.common.keys import Keys # permite vc escrever no navegador
from selenium.webdriver.common.by import By # permite vc escolher itens no navegador 

# Passo 1: Pegar a cotação do dólar


# Entrar no Google
navegador.get('https://www.google.com.br/')

# Pesquisar no google por cotação dolar
                                                                                                                  
navegador.find_element('xpath',
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
navegador.find_element('xpath',
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)


cotacao_dolar=navegador.find_element('xpath',
'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
# dentro do parêntes do attribute coloca-se a informação que vc quer pegar 
# usando o especionar 
print(cotacao_dolar)

## Cotação Euro

# Entrar no Google
navegador.get('https://www.google.com.br/')

# Pesquisar no google por cotação Euro
                                                                                                                  
navegador.find_element('xpath',
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element('xpath',
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro=navegador.find_element('xpath',
'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
# dentro do parêntes do attribute coloca-se a informação que vc quer pegar 
# usando o especionar 

print(cotacao_euro)


# Cotação Ouro 

# Entrar no Google
navegador.get('https://www.melhorcambio.com/ouro-hoje')

# Pesquisar no google por cotação ouro
                                                                                                                  
cotacao_ouro=navegador.find_element('xpath',
'//*[@id="comercial"]').get_attribute('value')# É .get pois apenas quero pegar uma informação 

cotacao_ouro = cotacao_ouro.replace(",",".") # Tratando, retirando a virgula e substituindo por ponto(.)
print(cotacao_ouro)

navegador.quit() # vai fechar o navegador