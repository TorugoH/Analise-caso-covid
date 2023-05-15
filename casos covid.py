import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('figure', figsize = (48,10))
dados = pd.read_csv('WHO-COVID-19-global-data.csv',sep=",")
numero_de_novos_casos = pd.DataFrame()
numero_de_novos_casos=dados[['Country','Cumulative_cases']]
numero_de_novos_casos = numero_de_novos_casos.groupby('Country').sum()
numero_de_novos_casos=numero_de_novos_casos.nlargest(10,'Cumulative_cases')
numero_de_novos_casos.reset_index(inplace=True)
plt.subplot(2, 2, 1)
fig  = sns.barplot(data=numero_de_novos_casos,x='Country',y='Cumulative_cases',color='green')
fig.set_title('Top 10 Paises com maiores casos de covid')
fig.set_xlabel('Pais')
fig.set_ylabel('Casos')

plt.subplot(2, 2, 2)
quantidade_de_mortes=dados[['Country','Cumulative_deaths']]
quantidade_de_mortes=quantidade_de_mortes.groupby('Country').sum()
quantidade_de_mortes=quantidade_de_mortes.nlargest(10,'Cumulative_deaths')
quantidade_de_mortes.reset_index(inplace=True)
fig_2 = sns.barplot(data=quantidade_de_mortes,x='Country', y='Cumulative_deaths',color='green')
fig_2.set_title('Top 10 pais com maiores perdas de vidas pela covid')
fig_2.set_xlabel('Paises')
fig_2.set_ylabel('Nº de mortes')

plt.subplot(2,2,3)
numero_casos_ano=dados[['Date_reported','New_cases']]
numero_casos_ano['Date_reported'] = numero_casos_ano['Date_reported'].astype('datetime64')
numero_casos_ano = numero_casos_ano.groupby([pd.Grouper(key='Date_reported',freq='Y')]).sum()
numero_casos_ano.reset_index(inplace=True)
numero_casos_ano['Date_reported']= numero_casos_ano['Date_reported'].dt.year

fig_3 = sns.lineplot(data=numero_casos_ano,x='Date_reported',y='New_cases',color='Green')
fig_3.set_xlabel('Ano',fontsize=12)
fig_3.set_ylabel('Casos confirmados',fontsize=12)
fig_3.set_title('Nº de casos por ano',fontsize=14)

plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.35)
plt.show()
