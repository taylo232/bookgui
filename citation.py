#!/usr/bin/env python3

import urllib.request
import time

def citquery(isbn):
    start = time.clock()
    myurl = "http://www.ottobib.com/isbn/" + str(isbn) + '/chicago'

    fp = urllib.request.urlopen(myurl)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()

    # get the pos of nearly there
    teststr = mystr.find('HANGING INDENT')
    
    if teststr == -1:
        citation = 'Not found'
    else:
        substr = mystr.find('<div class="nine columns">')
        # get pos of start of citation
        startpos = mystr.find('      ', substr) + 6

        # get pos of end of citation
        endpos = mystr.find('      ', startpos) -1

        # get citation
        citation = mystr[startpos:endpos]

        # remove <em> tags
        citation = citation.replace('<em>', '')
        citation = citation.replace('</em>', '')
        # print(citation)
        
    end = time.clock()
    qtime = "%.2g" % (end-start)

    bookreturn = (citation, qtime)
    return(bookreturn)


