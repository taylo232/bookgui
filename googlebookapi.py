#!/usr/bin/env python3
'''
Retrieving book information from the Google Book API using isbn
'''
from json import loads as json
from requests import get as api
import time


#######################
# isbn = '0330242822'
#######################

def gbquery(isbn):
    start = time.clock()
    
    api_query = '?q=isbn:' + isbn + '&format=json&jscmd=data'
    api_url = 'https://www.googleapis.com/books/v1/volumes'

    response = api(api_url + api_query) #response = api.get(api_url + api_query)
    api_response = json(response.content) #api_response = json.loads(response.content)
    thisbook = dict(api_response)

    try:
        booktitle = thisbook['items'][0]['volumeInfo']['title']
    except:
        booktitle = '?'

    try:
        bookauthor = thisbook['items'][0]['volumeInfo']['authors'][0]
    except:
        bookauthor = '?'

    try:
        bookdate = thisbook['items'][0]['volumeInfo']['publishedDate']
    except:
        bookdate = '?'

    try:
        bookpub = thisbook['items'][0]['volumeInfo']['publisher']
    except:
        bookpub = '?'

    try:
        bookpages = thisbook['items'][0]['volumeInfo']['pageCount']
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




