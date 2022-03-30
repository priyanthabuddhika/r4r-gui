from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore
from urllib.request import urlopen
import json
import pandas as pd
import random
from translate import translate, SINHALA, ENGLISH, TAMIL


#dictionary to store local pre-load parameters on a global level
parameters = {
    "lang": [],
    }

#global dictionary of dynamically changing widgets
widgets = {
    "labels" : [],
    "logo": [],
    "button": [],
    "nav": [],
    "message": [],
    "message2": []
}

#initialliza grid layout
grid = QGridLayout()
grid.setContentsMargins(80,24,80,24)

def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            for i in range(0, len(widgets[widget])):
                widgets[widget][i].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def clear_parameters():
    #clear the global dictionary of parameters
    for parm in parameters:
        if parameters[parm] != []:
            for i in range(0, len(parameters[parm])):
                parameters[parm].pop()

    parameters["lang"].append("en")

def start_navigation():

    #start, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    frameLangSelect()

def changeLang(locale):
    #start the app, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    parameters["lang"].append(locale)
    #display the home frame
    frameHome()

def homeFunc():
    clear_widgets()

def createLangSelectButton(locale):
    button = QPushButton()
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    button.setStyleSheet(
        f'''
        *{{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #229D16, stop:1 #1BB80D);
            border-radius: 12px 2px 2px 12px;
            color: 'white';
            width: 280px;
            height: 270px;
            margin-bottom: 50px;
        '''
        +
        "background-image : url(assets/lang/{subtitle}.png);}}".format(subtitle=locale)
    )
    #button callback
    button.clicked.connect(lambda: changeLang(locale))

    return button;

def createHomeButton(title, subtitle):
    button = QPushButton()
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        f'''
        *{{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #229D16, stop:1 #1BB80D);
            border-radius: 12px 2px 2px 12px;
            color: 'white';
            width: 280px;
            height: 270px;
        '''
        +
        "background-image : url(assets/home/{subtitle}.png);}}".format(subtitle=subtitle)
    )
    #button callback
    button.clicked.connect(lambda: homeFunc())

    return button;
    
def createNavButton(title):
    button = QPushButton()
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border-radius: 8px;
            color: 'white';
            width: 60px;
            max-width: 60px;
            height: 60px;
            background-image : url(assets/nav-home.png);
            }
        '''
    )
    #button callback
    button.clicked.connect(lambda: homeFunc())

    return button;
#*********************************************
#                  FRAME 1
#*********************************************

def frame1():
    clear_widgets()
    #logo widget
    image = QPixmap("assets/logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 70px;")
    widgets["logo"].append(logo)

    #button widget
    button = QPushButton("ENTER")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #229D16, stop:1 #1BB80D);
            border-radius: 12px 2px 2px 12px;
            font-size: 35px;
            color: 'white';
            padding: 25px 0;
            margin: 40px 150px;
        }
        '''
    )
    #button callback
    button.clicked.connect(start_navigation)
    widgets["button"].append(button)

    #place global widgets on the grid
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

#*********************************************
#           FRAME Language Select
#*********************************************

def frameLangSelect():
    clear_widgets()
    #logo widget
    image = QPixmap("assets/logo.png").scaled(140, 163, QtCore.Qt.KeepAspectRatio)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignLeft)
    widgets["logo"].append(logo)

    # Welcome text
    welcome1 = QLabel("WELCOME")
    welcome1.setStyleSheet(
        '''
         *{
            color: '#0DA400';
            font-size: 48px;
            font-weight: 700;
            margin-top: 20px;
          }
        '''
    )
    welcome1.setAlignment(QtCore.Qt.AlignRight)
    widgets["labels"].append(welcome1)

     # Welcome text
    welcome2 = QLabel("ආයුබෝවන් வணக்கம்")
    welcome2.setStyleSheet(
        '''
         *{
            color: '#787878';
            font-size: 29px;
            font-weight: 700;
            margin-top: 70px;
          }
        '''
    )
    welcome2.setAlignment(QtCore.Qt.AlignRight)
    widgets["labels"].append(welcome2)

    #button widget
    button = createLangSelectButton(ENGLISH)
    widgets["button"].append(button)

  #button widget
    buttonSi = createLangSelectButton(SINHALA)
    widgets["button"].append(buttonSi)

  #button widget
    buttonTa = createLangSelectButton(TAMIL)
    widgets["button"].append(buttonTa)

    #place global widgets on the grid
    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["button"][-3], 1, 0)
    grid.addWidget(widgets["button"][-2], 1, 1)
    grid.addWidget(widgets["button"][-1], 1, 2)
    grid.addWidget(widgets["labels"][-2], 0, 2, 1,3)
    grid.addWidget(widgets["labels"][-1], 0, 2,1,3)

#*********************************************
#           FRAME Home
#*********************************************

def frameHome():
    clear_widgets()
    #logo widget
    image = QPixmap("assets/logo.png").scaled(140, 163, QtCore.Qt.KeepAspectRatio)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignLeft)
    widgets["logo"].append(logo)

   
    # nav = QWidget()
    # layout = QHBoxLayout(nav)
    # # Add widgets to the layout
    # layout.addWidget(QPushButton("Left-Most"))
    # layout.addWidget(QPushButton("Center"), 1)

    nav = createNavButton("title")
    widgets["nav"].append(nav)

    #button widget
    scanIdButton = createHomeButton("title", "scan-id")
    widgets["button"].append(scanIdButton)

  #button widget
    newUserButton = createHomeButton("title", "new-user")
    widgets["button"].append(newUserButton)

  #button widget
    noIdButton = createHomeButton("title", "no-id")
    widgets["button"].append(noIdButton)

    #place global widgets on the grid
    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["button"][-3], 1, 0)
    grid.addWidget(widgets["button"][-2], 1, 1)
    grid.addWidget(widgets["button"][-1], 1, 2)
    grid.addWidget(widgets["nav"][-1], 0, 2, 1, 1, QtCore.Qt.AlignRight)



