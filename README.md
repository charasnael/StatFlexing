# Introduction

Disclaimer: This will only work if the metadatas of the books contained in the kobo are somewhat correct.

Also: Work in progress - feel free to create an issue or contribute if you wish a certain feature to be added 

The goal of this repository is to create an html page representative of the stats of Kobo's e-reader's database "KoboReader.sqlite" using google books' free API

Once the .json file has been created, the page can either be seen locally with the index-static.html file, or integrated to a website using the main.py file which uses python as a backend language to generate the webpage.

Written in python because most people can write code in python, I think.

For safety purposes, I recommend to make a copy of the sqlite database, even though the python will only read the database and not modify any content of it (data processing will be done on the json generated, not the database itself) 

## Setting up

Install the dependencies with the following command (using a virtual environment, or not):
```python
pip install -r ./requirements
```

Make sure the folder you're executing the code from has a file named "KoboReader.sqlite". If not, modify the variable named "filepath" at the beginning of the script in main.py

```python
python3 ./generate_json.py
```
Launching the backend:
```python
python3 ./main.py
```

# Video example


https://github.com/charasnael/StatFlexing/assets/75299103/38ab9b1e-767f-4b62-ac78-6837ba5b65ea



# Updating the json file

The script checks whether the entry is already present in the json file before querying 

# Adjustments

If you feel the data fetched by the json file is innacurate for some entries, you may manually modify a field of the file.

This includes: name of an image to use (by default ISBN_of_entry.jpg), thoughts of a book, series the book is a part of...

As the json grows bigger, existing entries will not be recreated (unless removed manually) - so your modifications will remain.


# Things I may or may not do:

## Project
- Delete unused files and clean the code a tiny bit

## Python
- 

## HTML
- Sort by "Series"
- Make the static page not look the way it does...
- Fix the arrows behaviour after a "sort by"
