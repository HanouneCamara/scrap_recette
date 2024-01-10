import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/recette/"

def get_text_if_not_none(e):
    if e:
        return e.text.strip() #strip() supprimer les espaces avant/apres la chaine de caractère 
    return None 

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
    
    description = get_text_if_not_none(soup.find("p", class_ = "description"))
    print(description)
    
    #ingrédients
    print("INGRÉDIENTS :")
    div_ingredients =  soup.find("div", class_ = "ingredients")
    e_ingredients = div_ingredients.find_all("p")
    for e_ingredient in e_ingredients:
        
        print(e_ingredient.text)
        
    
    #prepa
    print("PRÉPARATION :")
    div_preparation =  soup.find("div", class_ = "colonne2 colonne")
    e_preparations = div_preparation.find_all("td", class_ = "preparation_etape")
    for e_preparation in e_preparations:
        
        print(e_preparation.text)
    
    
else:
    print("ERREUR:", response.status_code)

print("FIN")