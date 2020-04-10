#!/usr/bin/env python3

import PySimpleGUI as sg
import googlebookapi as gb
import openlibraryapi as ol
import citation as cit

class Usarios:
    def __init__(self): #(self, isusario, nome, telefone, email, usario, senha):
        pass

    def insertUser(self):
        return 'User inserted'

layout =    [  

            [sg.Text('ISBN:', size=(10,1), justification='right'), 
            sg.Input(size=(20,1), key='sgISBN', do_not_clear=False), 
            sg.Button('Find'), sg.Button('Clear'),
            #sg.Text('hh', size=(100,1))],
            sg.Text('', size=(4,1)),
            sg.T('ISBN:', size=(10,1), justification='right'), 
            sg.I(key='isbndisplay', do_not_clear=False, size=(20,1), background_color='peachpuff')],
            [sg.Text('', size=(115,1))],

            [sg.Text('Google Books', size=(23,1), justification='right'),
            sg.Text('Open Library', size=(53,1), justification='right')],
            
            [sg.T('Title:', size=(10,1), justification='right'), sg.I(key='gTitle', do_not_clear=False, size=(42,1)),
            sg.T('Title:', size=(10,1), justification='right'), sg.I(key='oTitle', do_not_clear=False, size=(42,1))],

            [sg.T('Author:', size=(10,1), justification='right'), sg.I(key='gAuthor', do_not_clear=False, size=(42,1)),
            sg.T('Author:', size=(10,1), justification='right'), sg.I(key='oAuthor', do_not_clear=False, size=(42,1))],


            [sg.T('Publisher:', size=(10,1), justification='right'), sg.I(key='gPub', do_not_clear=False, size=(42,1)),
            sg.T('Publisher:', size=(10,1), justification='right'), sg.I(key='oPub', do_not_clear=False, size=(42,1))],


            [sg.T('Date:', size=(10,1), justification='right'), sg.I(key='gDate', do_not_clear=False, size=(42,1)),
            sg.T('Date:', size=(10,1), justification='right'), sg.I(key='oDate', do_not_clear=False, size=(42,1))],

            [sg.Text('', size=(115,1))],
            [sg.T('Citation:', size=(10,1), justification='right'), sg.I(key='cit', do_not_clear=False, size=(98,1))],
            
            [sg.Text('', size=(100,1))]
            ]

window = sg.Window('RJT Book Finder', layout, font='Calibri 10', default_element_size=(25,1)) #, location=(2700,100))

while True:
    event, values = window.read()
    
    if event is None:
        break

    if event == 'Find':
        isbn = values['sgISBN'] #    window['gTitle'].Update(isbn)
        
        if (isbn == '') or (isbn.isnumeric() == False):
            sg.popup('Please enter an ISBN.') #, location=(2700, 100))
        else:
            window['isbndisplay'].Update(isbn)
            
            glbook = gb.gbquery(isbn)
            olbook = ol.olquery(isbn)
            citation = cit.citquery(isbn)

            window['gTitle'].Update(glbook[0])
            window['gAuthor'].Update(glbook[1])
            window['gDate'].Update(glbook[2])
            window['gPub'].Update(glbook[3])
            
            window['oTitle'].Update(olbook[0])
            window['oAuthor'].Update(olbook[1])
            window['oDate'].Update(olbook[2])
            window['oPub'].Update(olbook[3])

            window['cit'].Update(citation[0])
    
    if event == 'Clear':

        # Clear all the boxes inc ISBN
        window['gTitle'].Update('')
