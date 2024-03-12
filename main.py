import sqlite3, json
from datetime import timedelta
from getInfos import getInfosFromTitle, correctSeries
import os.path
import time

def value_exists(value, list_of_dicts):
    for dictionary in list_of_dicts:
        if value in dictionary.values():
            return True
    return False

filepath="./KoboReader.sqlite"
jsonpath="./readbooks.json"
queryReadBooks = "select Attribution, Title, DateLastRead, Series, TimeSpentReading   from content WHERE ___PercentRead like 100 AND TimeSpentReading > 0;"
queryReadBooksKeys = ["Author","Title","Date Read", "Series","ReadFor"]
if __name__ == '__main__':
    listReadBooks=list()
    booksToAdd=list()
    # Connecting to the sqlite file
    con = sqlite3.connect(filepath)
    cur = con.cursor()
    result = cur.execute(queryReadBooks)
    # __________________FETCHING READ BOOKS FROM DATABASE_____________________
    for item in result.fetchall():
            listReadBooks.append(dict(zip(queryReadBooksKeys,item)))
            # Adding a key to convert seconds to hh:mm:ss. Leaving the original key for easier parsing in the future
            listReadBooks[-1]['ReadForFormatted'] = str(timedelta(seconds=listReadBooks[-1]['ReadFor']))
    #___________________CHECKING FOR EXISTING JSON FILE___________________
    if os.path.isfile(jsonpath):
        print("readbooks.json detected, checking keys to only query the API if the entry is new")
        with open(jsonpath, 'r', encoding='utf8') as file:
            existingJSON = json.load(file)
            
        # FOR ADDED ENTRIES IN COMPARISON TO EXISTING JSON 
        for item in listReadBooks:
            if not (value_exists(item['Title'], existingJSON)):
                
                #  getting metadata for new entry
                item=getInfosFromTitle(item)
                item=correctSeries(item)
                # adding the new entry to the existing json (or not)
                existingJSON.append(item)
                
                #  to not get timed out from google 
                time.sleep(1.1)
        # Updating existing file
        with open(jsonpath, 'w', encoding='utf8') as json_file:
            json.dump(existingJSON, json_file, ensure_ascii=False)
            
    # ___________________NO JSON FILE FOUND, CREATING ONE FROM SCRATCH___________________
    else:
        print("No 'readbooks.json' file detected, creating one from scratch. This might take a while")
        for item in listReadBooks:
            item=getInfosFromTitle(item)
            booksToAdd.append(item)
            item=correctSeries(item)
        # Writes the created list into the file as json
        with open(jsonpath, 'w', encoding='utf8') as json_file:
            json.dump(booksToAdd, json_file, ensure_ascii=False)
    
    con.close()
