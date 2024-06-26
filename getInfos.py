import requests, json, os.path
from datetime import datetime


def queryGoogleFromTitle(Booktitle, Bookauthor):
    url = "https://www.googleapis.com/books/v1/volumes?q={booktitle}%20{bookauthor}".format(booktitle=Booktitle, bookauthor=Bookauthor )
    print(url)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response

def getImageFromURL(book):
    if book['ISBN'] and book['bookCover'] and not(os.path.isfile("images/"+book['ISBN']+'.jpg')):
        print("Found url & ISBN for current book: ", book['Title'])
        url = book['bookCover']
        file_name = str("static/"+book['ISBN']+'.jpg')
        data = requests.get(url).content
        f = open(file_name, 'wb')
        f.write(data)
        f.close()
    

def getInfosFromTitle(book):
    bookInfos = queryGoogleFromTitle(book['Title'], book['Author'])
    if bookInfos.status_code == 200:
        infos=json.loads(bookInfos.text)
        print(infos['items'][0])
        print("_________________________________")
        print("_________________________________")
        print("_________________________________")
        print(infos['items'][1])
        try:
            bookISBN = infos['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier']
            print(bookISBN)
            book['ISBN'] = bookISBN
        except:
            print("Could not retrieve book's ISBN")
        try:
            bookCategory = infos['items'][0]['volumeInfo']['categories']
            print(bookCategory)
            book['category'] = bookCategory
        except:
            print("Could not retrieve book's category")
        try:
            bookPageCount = infos['items'][0]['volumeInfo']['pageCount']
            print(bookPageCount)
            book['pageCount'] = bookPageCount
        except:
            print("Could not retrieve book's page count")
        try:
            try:
              bookCover = infos['items'][0]['volumeInfo']['imageLinks']['large']
            except:
              bookCover = infos['items'][0]['volumeInfo']['imageLinks']['thumbnail']
            book['bookCover'] = bookCover
            getImageFromURL(book)
            print(bookCover)
        except:
            print("Could not retrieve book's cover")
        try:
            bookLanguage = infos['items'][0]['volumeInfo']['language']
            print(bookLanguage)
            book['Language'] = bookLanguage
        except:
            print("Could not retrieve book's language")
    else:
        print("Status code != 200, skipping book")
    return book

def correctSeries(book):
    if book['Series'] is None :
        print ("No series for ", book['Title'], "correcting the entry" )
        book['Series'] = ""
    return book
def correctDateRead(book):
    print('Adding column DateReadFormatted')
    try:
        date_object = datetime.strptime(book['Date Read'], "%Y-%m-%dT%H:%M:%S.%f")
        print(date_object.strftime("%d/%m/%Y"))
        book['DateReadFormatted'] = date_object.strftime("%d/%m/%Y")
    except:
        date_object = datetime.strptime(book['Date Read'], "%Y-%m-%dT%H:%M:%SZ")
        print(date_object.strftime("%d/%m/%Y"))
        book['DateReadFormatted'] = date_object.strftime("%d/%m/%Y")        
    return book
def correctThoughts(book):
    if book.get('Thoughts') is None :
        print ("No Thoughts key for ", book['Title'], "correcting the entry" )
        book['Thoughts'] = ""
    return book