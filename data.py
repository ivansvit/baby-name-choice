from bs4 import BeautifulSoup
import requests

URL = "https://www.nostrofiglio.it/gravidanza/nomi-per-bambini/i-50-nomi-per-bambine-piu-popolari-del-web"

response = requests.get(url=URL)
babies_names_webpage = response.text

our_list_of_names = ['Dariya', 'Ilaria', 'Michela', 'Naomi']

soup = BeautifulSoup(babies_names_webpage, "html.parser")
nomi = soup.find_all(name="li")
names_girls = [name.getText().replace(u'\xa0', u'').replace(",", "").replace(".", "") for name in nomi][22:148]
names_girls.extend(our_list_of_names)
print(len(names_girls))
# Clean data from duplicates
names_girls = list(dict.fromkeys(names_girls))
print(len(names_girls))