#!/usr/bin/env python
# coding: utf-8

# API 
# 
# Api - usa-se em tudo para se percorrer as rotas da internet;
# 
# Endpoint -> É uma extremidade de um servidor;
# 
# Api's -> forma de dois sistemas se comunicarem 
# 
# Json -> Formato das requisições
# 
# 

# In[ ]:





# In[ ]:





# Requisiçoes 
# 
# Get -> usado para acessar dados do servidor, para acessar qualquer site 
# 
# Post -> Voce está envioando dados para o servidor e para postar comentários 
# 
# Delete -> Deleta coisas no servidor 
# 
# Put -> São usadas para atualizar dados no servidor
# 
# 

# In[1]:


import requests 
import pandas as pd 
import json 


# In[2]:


info_google = requests.get('https://www.google.com.br/')

print(info_google)


# In[7]:


#info_google.text
#info_google.json()
#info_google.headers


# In[12]:


codico = 432

url_banco_central = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codico}/dados?formato=json'


# In[13]:


dados_selic = requests.get(url_banco_central)
print(dados_selic.json())


# In[14]:


json_selic = dados_selic.json()


# In[15]:


df = pd.DataFrame(json_selic)


# In[16]:


df


# In[31]:


import matplotlib.pyplot as plt
plt.gca().invert_yaxis()

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')

plt.plot(df['data'], df['valor'])
plt.xlabel('Data')
plt.ylabel('Valor')
plt.title('Selic na série temporal ')

plt.show()


# #Método Post 
# 
# Biblioteca JSON 
# 

# In[28]:


dicionario_cotacoes= {'WEGE3': [20,30,40], 'VALE3': [20,45,60]}

dicionario_cotacoes


# In[30]:


json_cotacoes = json.dumps(dicionario_cotacoes)

json_cotacoes


# In[32]:


# Requisicao da inflacao da inflacao por uma api 

codico = 433

url_banco_central_inflacao = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codico}/dados?formato=json'


# In[36]:


# Importando dados de API do banco central mês a mês

dados_Inflacao = requests.get(url_banco_central_inflacao)
dados_Inflacao.json()


# In[40]:


dInflacao = dados_Inflacao.json()
dataFrameInflação = pd.DataFrame(dInflacao)


# In[41]:


dataFrameInflação


# In[ ]:





# In[ ]:





# In[ ]:




