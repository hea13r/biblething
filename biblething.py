import requests
import json

def apiGetter(book):
    url = "https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/en-asv/books/" + book + "/chapters/2.json"
    resource = requests.get(url)
    resourceJson = resource.json()
    return resourceJson

def bookWriter(rJson):
    book = ""
    for i in rJson['data']:
        book += i['text'] + '\n'
    return book

def main():
    print("This program is meant to return books of the bible without chapter or verse labels")
    book = input("Enter the book you would like to retrieve|>")
    bookText = bookWriter(apiGetter(book))
    with open(book + '.txt', 'w') as f:
        f.write(bookText)

main()
