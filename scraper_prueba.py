import boto3
import requests
from datetime import datetime

# URLs a descargar
urls = ['https://www.eltiempo.com/', 'https://www.elespectador.com/']

# Formato = s3://bucket/headlines/raw/contenido-yyyy-mm-dd.html
newspapers = ['el_tiempo', 'el_espectador']

# Fecha actual
now = datetime.now()
date = now.strftime('%Y-%m-%d')



for url, newspaper in zip(urls, newspapers):
    response = requests.get(url)
    html_content = response.text
    with open(f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-raw/{newspaper}/contenido-{date}.html', 'w') as f:
        f.write(html_content)