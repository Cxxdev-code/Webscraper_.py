import requests
from bs4 import BeautifulSoup
import json
import re


class Pessoa:
    def __init__(self, nome, localidae):
        self._nome = nome
        self._localidade = localidae
        
    @property
    def nome(self,):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @property
    def localidade(self):
        return self._localidade
    
    @localidade.setter
    def localidade(self, regiao):
        self._localidade = regiao
        
class Scraper:
    
    
    def __init__(self, Regiao):
        self._regiao = Regiao
        self._url =  f"https://www.climaeradar.com.br/previsao-tempo/"
        self.request = requests.Session()
        
        
    def Caminho_url(self,):
        return  self._url + self._regiao


    def Requisicao(self):
        url = self.Caminho_url()
        self.html = self.request.get(url).text
        self.suop = BeautifulSoup( self.html , "html.parser")
        
        
    def dados_extraidos(self):
        
        tag = self.suop.find_all("script")
        for script in tag:
            texto = script.text
            if "weatherstationreport/nearby/v2" in texto:
                string = texto

                match = re.search(
                    r'"https://api-web\.wo-cloud\.com/weatherstationreport/nearby/v2[^"]*":\s*(\[[^\]]+\])',string)
                
                if match:
                    dados = json.loads(match.group(1))
                    return dados[0]

                raise ValueError("Dados de clima não encontrados no HTML.")
        
        







