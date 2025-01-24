### Dentro da pasta
- pip install pandas
- pip install openpyxl
- pip install pywin32

### Códigos pré-prontos para enviar o email via outlook
- import win32.com.client as win32

- outlook = win32.Dispatch('outlook.application')
- mail = outlook.CreateItem(0)
- mail.To = 'kroidaarkhamdragon@outlook.com'
- mail.Subject = 'Relatório de Vendas por Loja'
- mail.HTMLBody = '<h2> </h2>'

- mail.Send()