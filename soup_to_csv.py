from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
date = now.strftime('%Y-%m-%d')
link_head_el_tiempo = 'https://www.eltiempo.com'
link_head_el_espectador = 'https://www.elespectador.com'

def extract_tiempo(doc_el_tiempo):

    with open(doc_el_tiempo) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    headlines = soup.find_all(class_='title page-link')
    print(len(headlines))
    for headline in headlines:
        title = headline.text
        headless_link = headline['href']
        category = headless_link.split('/')[1]
        full_link = f''



doc_el_espectador = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-raw/el_espectador/contenido-{date}.html'
doc_el_tiempo = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-raw/el_tiempo/contenido-{date}.html'

extract_tiempo(doc_el_tiempo)





