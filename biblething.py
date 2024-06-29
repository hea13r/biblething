import requests
import json

# This function makes the call for the book of the bible and chapter requested
# It will also raise an exception when the chapter goes beyond what is possible, which will end the later loop
def apiGetter(book, chapter):
    # This if statement removes the space for books like 1 john so they will be retrieved successfully
    if " " in book:
        book = book.replace(" ", "")
    url = f"https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/en-asv/books/{book}/chapters/{chapter}.json"
    resource = requests.get(url)
    if resource.status_code != 200:
        raise Exception("There are no more chapters in this book")
    else:
        return resource.json()

# This function runs a loop through the chapter to return only the verses with a newline at the end of each verse
def bookWriter(rJson):
    book = ""
    for i in rJson['data']:
        book += i['text'] + '\n'
    return book

def main():
    print("This program is meant to return books of the bible without chapter or verse labels")
    book = input("Enter the book you would like to retrieve|>")
    chapter = 1
    bookText = f"{book.capitalize()}\n\n"
    isValid = True
    # This loop makes a request for every chapter in the requested book and appends them to the bookText
    # When the loop ends, after all chapters are retrieved, it writes them to a new file in whatever directory the program was run in
    while isValid:
        try:
            bookText += bookWriter(apiGetter(book, chapter))
            print(f"Getting chapter {chapter}...") # adds a print for every chapter, otherwise it looks like it's just a hung process or something
            chapter += 1
        except Exception:
            chapter -= 1 # because the chapter will be at one more than the number of chapters in the book at this point so we need to decrement by one
            print(f"{chapter} is the last chapter in this book.") # just a little extra verbosity
            print("Ending.")
            isValid = False
    with open(book + '.txt', 'w') as f:
        f.write(bookText)

if __name__ == "__main__":
    main()
