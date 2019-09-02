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

        #lineEdit
        self.line1 = self.findChild(QLineEdit, 'lineEdit_1')
        self.line2 = self.findChild(QLineEdit, 'lineEdit_2')

        # buttons
        self.button = self.findChild(QPushButton, 'pushButton_1')
        self.button.clicked.connect(self.bar)

        # labels
        self.lbl_errors = self.findChild(QLabel, 'label_5')
        self.lbl_correct = self.findChild(QLabel, 'label_3')
        self.lbl_len = self.findChild(QLabel, 'label_2')

        self.show()

    def convertArrayToStr(arr):
        strIng = ''
        for a in arr:
            strIng += a + ' '
        return strIng

    def correct(self, inputVar):
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

            correctCount = len(sentenceSplitter)
            lenOfsentence = len(sentenceSplitter)
            for n, s in enumerate(sentenceSplitter):
                for n2, x in enumerate(targetWords):
                    if str(s) == x[0]:
                        errorCount += 1
                        correctCount -= 1
                        sentenceSplitter[n] = x[1]
            return (
            convertArrayToStr(sentenceSplitter), errorCount, correctCount, lenOfsentence
         )
        except Exception as e:
            print('we have error in ', e)

    def bar(self):

        new, errorCount, correctCount, lenOfsentence = self.correct(self.line1.text())

        self.line2.setText(new)
        print(errorCount, correctCount, lenOfsentence)
            # set text to labels
       # self.lbl_errors.setText(errorCount)
       # self.lbl_correct.setText(correctCount)
       # self.lbl_len.setText(lenOfsentence)







def main():
    app = QApplication(argv)
    window = Main()
    window.show()
    exit(app.exec_())
if __name__ == "__main__":
    main()
