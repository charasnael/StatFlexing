from getInfos import correctSeries, correctDateRead, correctThoughts
import os.path
import json

jsonpath="./readbooks.json"
queryReadBooks = "select Attribution, Title, DateLastRead, Series, TimeSpentReading   from content WHERE ___PercentRead like 100 AND TimeSpentReading > 0;"
queryReadBooksKeys = ["Author","Title","Date Read", "Series","ReadFor"]
if __name__ == '__main__':
    listReadBooks=list()
    if os.path.isfile(jsonpath):
        print("readbooks.json detected, correcting entries where series = null")
        with open(jsonpath, 'r', encoding='utf8') as file:
            existingJSON = json.load(file)
            
        for item in existingJSON:
            item=correctSeries(item)
            item=correctDateRead(item)
            item=correctThoughts(item)
            listReadBooks.append(item)
            
        # Updating existing file
        with open(jsonpath, 'w', encoding='utf8') as json_file:
            json.dump(listReadBooks, json_file, ensure_ascii=False)
            
    # ___________________NO JSON FILE FOUND, CREATING ONE FROM SCRATCH___________________
    else:
        print("No 'readbooks.json' file detected, please generate one using the 'main.py' script")
