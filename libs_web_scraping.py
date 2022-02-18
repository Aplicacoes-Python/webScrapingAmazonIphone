import time
import requests
from bs4 import BeautifulSoup
from requests_config import url
from requests_config import headers
import pandas as pd


def request_url(timeout=60):

    # Loop de retentativa para realizar o request
    for _ in range(timeout):

        # Realiza o request
        response_url = requests.get(url, headers=headers)

        # Captura o status code referente ao request realizado
        status_code_request = response_url.status_code

        # Caso tenha obtido status_code 200, retorna o response obtido
        if status_code_request == 200:
            return response_url

        # Caso contrário, há o delay para tentar fazer o request novamente
        time.sleep(0.5) 

def search_iphone_url(body_response):
    list_descricao_aparelhos = []
    list_valor_aparelhos = []
    
    # Cria o objeto soup
    soup = BeautifulSoup(body_response.text, 'html.parser')

    # Procura pela div de cada aparelho retornado na pesquisa
    resultado_pesquisa = soup.find_all('div', {'class':'a-section a-spacing-small s-padding-left-small s-padding-right-small'})
    
    # Para cada aparelho(div), capturaremos a descrição e o valor e atribuimos ao dicionário 
    for aparelho in resultado_pesquisa:
        descricao_aparelho = aparelho.find('span', {'class':'a-size-base-plus a-color-base a-text-normal'})
        preço_aparelho = aparelho.find('span', {'class':'a-offscreen'})
        list_descricao_aparelhos.append(descricao_aparelho.text.replace(u'\xa0', u' '))
        if not preço_aparelho is None:
            list_valor_aparelhos.append(preço_aparelho.text.replace(u'\xa0', u' '))
        else:
            list_valor_aparelhos.append("SEM VALOR")
    return list_descricao_aparelhos, list_valor_aparelhos

def generate_sheet_output(descricoes, valores, path_output):
    dataframe = pd.DataFrame(data=list(zip(descricoes, valores)), columns=["Descricao", "Valor"])
    print(dataframe)
    dataframe.to_excel(path_output)
    print(f"generate_sheet_output() - Planilha gerada com sucesso para o path: {path_output}")