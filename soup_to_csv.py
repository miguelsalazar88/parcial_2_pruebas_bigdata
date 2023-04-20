from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
date = now.strftime('%Y-%m-%d')
link_head_el_tiempo = 'https://www.eltiempo.com'
link_head_el_espectador = 'https://www.elespectador.com'
doc_el_espectador = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-raw/el_espectador/contenido-{date}.html'
doc_el_tiempo = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-raw/el_tiempo/contenido-{date}.html'

csv_el_espectador = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-final/el_espectador/contenido-{date}.csv'
csv_el_tiempo = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-final/el_tiempo/contenido-{date}.csv'

def extract_tiempo(doc_el_tiempo, csv_el_tiempo):

    with open(doc_el_tiempo) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    headlines = soup.find_all(class_='title page-link')
    with open(csv_el_tiempo, 'w') as csv:
        csv.write('categoria, titular, enlace\n')
        for headline in headlines:
            title = headline.text
            headless_link = headline['href']
            category = headless_link.split('/')[1]
            full_link = f'{link_head_el_tiempo}{headless_link}'
            csv.write(f'{category},{title},{full_link},\n')

def extract_espectador(doc_el_espectador, link_el_espectador):
    with open(doc_el_espectador) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    headlines = soup.find_all("h2", class_="Card-Title Title Title")
    with open(csv_el_espectador, 'w') as csv:
        csv.write('categoria, titular, enlace\n')
        for headline in headlines:
            title = headline.text
            headless_link = headline.find("a")["href"]
            category = headless_link.split('/')[1]
            full_link = f'{link_head_el_espectador}{headless_link}'
            csv.write(f'{category},{title},{full_link},\n')
            

doc_el_espectador = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-raw/el_espectador/contenido-{date}.html'
doc_el_tiempo = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-raw/el_tiempo/contenido-{date}.html'

csv_el_espectador = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-final/el_espectador/contenido-{date}.csv'
csv_el_tiempo = f'/Users/miguelsalazar/Desktop/big_data/parcial2/headlines-final/el_tiempo/contenido-{date}.csv'

# extract_tiempo(doc_el_tiempo, csv_el_tiempo)
extract_espectador(doc_el_espectador, csv_el_espectador)





