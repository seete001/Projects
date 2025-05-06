import requests
from bs4 import BeautifulSoup


url = 'https://www.scrapethissite.com/pages/simple/'

r = requests.get(url=url, headers={}, timeout=10)
soup = BeautifulSoup(r.text, 'html.parser')

lands = soup.find_all('div', class_="col-md-4 country")
for i,land in enumerate(lands, 1):
    land_tag = land.find('h3', class_='country-name')
    land_name = land_tag.get_text(strip=True)
    land_capital = land_tag.find('span', class_='country-capital')
    land_population =  land_tag.find('span', class_='country-population')
    land_area = land_tag.find('span', class_='country-area')
    print(i,' ', land_name)