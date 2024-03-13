# Introduction

Disclaimer: This will only work if the metadatas of the books contained in the kobo are somewhat correct.

Also: Work in progress

The goal of this repository is to create a static html page representative of the stats of Kobo's e-reader's database "KoboReader.sqlite".

Written in python because most people can write code in python, I think.

For safety purposes, I recommend to make a copy of the sqlite database, even though the python will only read the database and not modify any content of it (data processing will be done on the json generated, not the database itself) 

## To do:

### python

- Format the "read on" date to something readable

### HTML
- Sort by "Series"


## Setting up

Create a python virtual environment (or don't) and install the dependencies with the following command:
```python
pip install -r requirements.txt
```

Make sure the folder you're executing the code from has a file named "KoboReader.sqlite". If not, modify the variable named "filepath" at the beginning of the script in main.py