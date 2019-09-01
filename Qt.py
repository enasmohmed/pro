import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import exit, argv

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUiType
from PyQt5.uic.properties import QtWidgets
from pyarabic import araby

from test import convertArrayToStr

main_ui,_ = loadUiType("prevew.ui")

class Main(QMainWindow , main_ui):
    def __init__(self , parent = None):
        super(Main, self).__init__( parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.line1 = self.findChild(QLineEdit, 'lineEdit_1')
        self.line2 = self.findChild(QLineEdit, 'lineEdit_2')
        self.button = self.findChild(QPushButton, 'pushButton_1')
        self.button.clicked.connect(self.bar)
        self.show()

    def convertArrayToStr(arr):
        strIng = ''
        for a in arr:
            strIng += a + ' '
        return strIng

    def correct(inputVar):
        targetWords = [
            ['احمد', 'أحمد'],
            ['المدرسه', 'المدرسة'],
            ['الي', 'إلى'],
            ['شاطئ', 'شاطيء'],
            ['بادئ', 'باديء'],
            ['ناشئ', 'ناشيء'],
            ['لاجئ', 'لاجيء'],
        ]
        try:
            inputVar = str(inputVar)
            errorCount = 0
            sentenceSplitter = araby.tokenize(inputVar)
            print(sentenceSplitter)
            correctCount = len(sentenceSplitter)
            lenOfsentence = len(sentenceSplitter)
            for n, s in enumerate(sentenceSplitter):
                for n2, x in enumerate(targetWords):
                    if str(s) == x[0]:
                        errorCount += 1
                        correctCount -= 1
                        sentenceSplitter[n] = x[1]
            print(convertArrayToStr(sentenceSplitter))
            print('Wrong : {}, Correct : {}, Total : {}'.format( \
                errorCount, correctCount, lenOfsentence))
        except Exception as e:
            print('we have error in ', e)

    def bar(self):
        #new =self. correct()
        #new = self.correct(self.line.text())
        #self.line2.setText(new)
        #print(self.line.text())
        print(self.correct(self.line1.text()))

        #return('Wrong : {}, Correct : {}, Total : {}'.format( \
            #errorCount, correctCount, lenOfsentence))

def main():
    app = QApplication(argv)
    window = Main()
    window.show()
    exit(app.exec_())
if __name__ == "__main__":
    main()

