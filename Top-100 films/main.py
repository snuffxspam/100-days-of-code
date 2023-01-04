import requests
import lxml
import random
from bs4 import BeautifulSoup


url = "https://www.ivi.ru/collections/top-100-best-movies"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

films = soup.find_all(class_="nbl-slimPosterBlock__titleText")
film_name = []
for i in films:
    film_name.append(i.getText())

print(random.choice(film_name))