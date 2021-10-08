from googletrans import Translator
from googletrans import LANGUAGES
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *

app = QtWidgets.QApplication([])
window = uic.loadUi("design.ui")

print(LANGUAGES)
for lang in LANGUAGES: # 'code':'full name'
    window.dropDown.addItem(LANGUAGES[lang].capitalize())

translator = Translator(service_urls=['translate.googleapis.com'])
# translation = translator.translate("Hey everyone you doing?",dest="hi")

# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

def get_key(val):
    for key, value in LANGUAGES.items():
         if val == value:
             return key
def changeLang(text,d):
    return translator.translate(text,dest=get_key(d))

def changeBtn():
    text = window.textBox.toPlainText()
    dest = window.dropDown.currentText()
    window.textBox2.setPlainText(changeLang(text,dest))

def main():
    window.btn.clicked.connect(changeBtn)
main()
window.show()
app.exec()