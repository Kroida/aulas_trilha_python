# Importar a base de dados
import pandas as pd
import win32com.client as win32

tabela_de_vendas = pd.read_excel('Vendas.xlsx')

# Visualizar a base de dados
pd.set_option('display.max_columns', None)
# print(tabela_de_vendas)

# Faturamento por loja
faturamento = tabela_de_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
# print('-' * 50, faturamento, sep='\n')

# Quantidade de produtos vendidos por loja
quantidade = tabela_de_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
# print('-' * 50, quantidade, sep='\n')

# Tickect médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame() # Dividiu coluna por coluna e transformou em DataFrame
# print('-' * 50, ticket_medio, sep='\n')

# Enviar um email com o relatório anexado
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'luisGNS8022@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>
<p>Segue o Relatório de Vendas por cada Loja.</p>
<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}
<p>Quantidade Vendida:</p>
{quantidade.to_html()}
<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}
<p>Qualquer dúvida estou à disposição.</p>
<p>Att.,</p>
<p>Luis</p>
'''

mail.Send()

print('Email Enviado')