from googletrans import Translator
from googletrans import LANGUAGES
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *

app = QtWidgets.QApplication([])
window = uic.loadUi("design.ui")

window.setMaximumWidth(770)
window.setMaximumHeight(406)
window.setMinimumWidth(770)
window.setMinimumHeight(406)
for lang in LANGUAGES: # 'code':'full name'
    window.dropDown.addItem(LANGUAGES[lang].capitalize())
translator = Translator(service_urls=['translate.googleapis.com'])

def get_key(val):
    for key, value in LANGUAGES.items():
         if val.lower() == value:
             return key

def changeLang(text,d):
    chng=translator.translate(text,d)
    return chng.text

def changeBtn():
    text = window.textBox.toPlainText()
    dest = window.dropDown.currentText()
    window.textBox2.setPlainText(changeLang(text,get_key(dest)))

def main():
    window.btn.clicked.connect(changeBtn)

main()
window.show()
app.exec()