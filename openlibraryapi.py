#!/usr/bin/env python3
'''
Retrieving book information from the OpenLibrary API
They have gaps. Might need to use GoogleBooks instead
'''
from json import loads as json
from requests import get as api
import time


#######################
# isbn = '0330242822'
#######################

def olquery(isbn):
    start = time.clock()
    bookisbn = 'isbn:' + isbn
    api_query = '?bibkeys=' + bookisbn + '&format=json&jscmd=data'
    api_url = 'https://openlibrary.org/api/books'

    response = api(api_url + api_query) #response = api.get(api_url + api_query)
    api_response = json(response.content) #api_response = json.loads(response.content)
    thisbook = dict(api_response)

    # because empty fields are not returned
    try:
        booktitle = thisbook[bookisbn]['title']
    except:
        booktitle = '?'

    try:
        bookauthor = thisbook[bookisbn]['authors'][0]['name']
    except:
        bookauthor = '?'

    try:
        bookdate = thisbook[bookisbn]['publish_date']
    except:
        bookdate = '?'

    try:
        bookpub = thisbook[bookisbn]['publishers'][0]['name']
    except:
        bookpub = '?'

    try:
        bookdate = thisbook[bookisbn]['publish_date']
    except:
        bookdate = '?'

    try:
        bookpages = thisbook[bookisbn]['number_of_pages']
    except:
        bookpages = '?'

    # print('Title =', booktitle)
    # print('Author =', bookauthor)
    # print('Date =', bookdate)
    # print('Publisher =', bookpub)
    # print('Pages =', bookpages)

    # print("---------------------------------")
    end = time.clock()
    qtime = "%.2g" % (end-start)

    bookreturn = (booktitle, bookauthor, bookdate, bookpub, bookpages, qtime)
    return(bookreturn)