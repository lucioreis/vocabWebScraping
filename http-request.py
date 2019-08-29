import requests as rq
from bs4 import BeautifulSoup
from qtWebClient import Client

def get_page(url: str):
    return BeautifulSoup(Client(url).html, "html.parser")
# page = rq.get("https://translate.google.com/?hl=pt-BR&tab=TT#view=home&op=translate&sl=en&tl=pt&text=ground")
google = "https://translate.google.com/?hl=pt-BR&tab=TT#view=home&op=translate&sl=en&tl=pt&text={word}"
longman = "https://www.ldoceonline.com/dictionary/{word}"
marriam = "https://www.merriam-webster.com/dictionary/{word}"
words = ["ground", "let alone"]
words_longman = [word.replace(" ","-") for word in words]
words_google = [word.replace(" ","%20") for word in words]
words_merriam = [word.replace(" ","%20") for word in words]

for word in words:
    bs = get_page(url)

    definitions = [tag.text.lstrip().rstrip() for tag in bs.find_all(class_="DEF")]
    phrases = [tag.text.lstrip().rstrip() for tag in bs.find_all(class_="EXAMPLE")]

    print(('{}\n'*len(definitions)).format(*definitions))
    print(('{}\n'*len(phrases)).format(*phrases))
    for i in range(10):
        try:
            print("Attempt number {}".format(i))
            response = rq.get("https://www.ldoceonline.com/dictionary/{word}".format(word=word))
            break
        except rq.exceptions.ConnectionError:
            print("Connection Error please try again.")
            exit(101)

    if response.status_code == 404:
        print("Not found page for word {word}".format(word=word))
    elif response.status_code == 200:
        print("Success!")

    bs = BeautifulSoup(response.content, "html.parser")
    definitions = [tag.text for tag in bs.find_all(class_="DEF")]
    phrases = [tag.text for tag in bs.find_all(class_="EXAMPLE")]
    print(definitions)
    print(phrases)
