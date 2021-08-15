# importando bibliotecas que serão utilizadas
import pandas as pd
import matplotlib.pyplot as plt

# iniciando o documento csv na plataforma Pycharm
df = pd.read_csv('Gapminder.csv', sep=';')

# verificando os dados contidos no arquivo csv
'''print(df.head())
print(df.tail())
print(df.dtypes)'''

# transformando coluna data no tipo datetime
df['year'] = pd.to_datetime(df['year'])
'''print(df.dtypes)'''

# verificando valores vazios
'''print(df.isnull().sum())'''

# substituindo os valores vazios por 0
df['continent'].fillna(0, inplace=True)
'''print(df.isnull().sum())'''

# Comparações
# selecionando país

pais = str(input('Select a country: '))
df_pais = df[df['country'] == pais]
'''print(df_pais.head())'''

lista_pais_exp = df_pais['lifeExp'].to_list()
lista_pais_gdp = df_pais['gdpPercap'].to_list()
lista_pais_pop = df_pais['pop'].to_list()

plt.plot(lista_pais_exp, lista_pais_gdp)
plt.xlabel('Expectativa de vida')
plt.ylabel('PIB')
plt.title('País: %s' % pais)
plt.show()
