import requests, json, os.path


def queryGoogleFromTitle(Booktitle):
    url = "https://www.googleapis.com/books/v1/volumes?q={booktitle}".format(booktitle=Booktitle)
    print(url)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response

def getImageFromURL(book):
    if book['ISBN'] and book['bookCover'] and not(os.path.isfile("images/"+book['ISBN']+'.jpg')):
        print("Found url & ISBN for current book: ", book['Title'])
        url = book['bookCover']
        file_name = str("images/"+book['ISBN']+'.jpg')
        data = requests.get(url).content
        f = open(file_name, 'wb')
        f.write(data)
        f.close()
    

def getInfosFromTitle(book):
    bookInfos = queryGoogleFromTitle(book['Title'])
    if bookInfos.status_code == 200:
        infos=json.loads(bookInfos.text)
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
            print("Could not retrieve book's page count")
    else:
        print("Status code != 200, skipping book")
    return book

def correctSeries(book):
    if book['Series'] is None :
        print ("No series for ", book['Title'], "correcting the entry" )
        book['Series'] = ""
    return book