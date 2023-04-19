import boto3
import requests
from datetime import datetime

# URLs a descargar
urls = ['https://www.eltiempo.com/', 'https://www.elespectador.com/']

# Cliente de S3
s3 = boto3.client('s3')

# Fecha actual
now = datetime.now()

# Nombre del bucket y la carpeta dentro del bucket donde se almacenarán los archivos
bucket_name = 'headlines-raw'
folder_name = f'periodico=html/year={now.year}/month={now.month}/day={now.day}/'

# Iterar sobre las URLs y descargar el contenido HTML
for url in urls:
    response = requests.get(url)
    html_content = response.text
    
    # Subir el archivo a S3
    key_name = folder_name + url.split('/')[-2] + '.html'
    s3.put_object(Bucket=bucket_name, Key=key_name, Body=html_content)