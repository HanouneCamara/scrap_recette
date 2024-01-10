import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/recette/"

response = requests.get(url)
response.encoding = response.apparent_encoding #Encodage

if response.status_code == 200:
    html = response.text
    f = open("recette.html", "w")
    f.write(html)
    f.close()
    
    soup = BeautifulSoup(html, "html5lib")
    titre = soup.find("h1").text
    print(titre)
    
    description = soup.find("p", class_ = "description").text
    print(description)
    
    
    
else:
    print("ERREUR:", response.status_code)

print("FIN")