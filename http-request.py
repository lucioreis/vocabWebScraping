import requests as rq
from bs4 import BeautifulSoup
from qtWebClient import Client


# page = rq.get("https://translate.google.com/?hl=pt-BR&tab=TT#view=home&op=translate&sl=en&tl=pt&text=ground")
url = "https://translate.google.com/?hl=pt-BR&tab=TT#view=home&op=translate&sl=en&tl=pt&text=ground"
client_response = Client(url)
source = client_response.html
bs = BeautifulSoup(source, "html.parser")

phrases = [tag.text for tag in bs.find_all(class_="gt-def-row")]
print(('{}\n'*len(phrases)).format(*phrases))
