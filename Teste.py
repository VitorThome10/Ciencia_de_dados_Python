import pandas as pd 
import numpy as np

def ferador_serie(valor_inicial,volatilidade,periodos,dia_inicial,frequencia ="M"):

     vetor = [valor_inicial]

     for i in range(periodos -1) :

         preco = vetor[i]* (1+np.random.normal(0,volatilidade))

         vetor.append(preco)
    
        serie = pd.Series(vetor,index = pd.date_range(dia_inicial,periods = periodos ,freq = frequencia))

     return serie 

serie_euro = gerador_serie(5,0.01,5,"2022-01-01")
serie_cotacoes = gerador_serie(20,0.05,5,"2022-02-01") #
serie_cotacoes