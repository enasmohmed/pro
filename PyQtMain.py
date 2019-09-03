from PyQt5.QtWidgets import *
from sys import argv

from PyQt5.QtWidgets import QMainWindow, QApplication

from pyarabic import araby

from main import Ui_MainWindow


class Main(QMainWindow , Ui_MainWindow):
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

        self.btn_save = self.findChild(QPushButton, 'pushButton_2')
        self.btn_save.clicked.connect(self.save_output)


        # labels
        self.lbl_errors = self.findChild(QLabel, 'label_5')
        self.lbl_correct = self.findChild(QLabel, 'label_3')
        self.lbl_len = self.findChild(QLabel, 'label_2')

        #self.show()

    def convertArrayToStr(self ,arr):
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
            ['الهندسيه', 'الهندسية'],
            ['المستويه', 'المستوية'],
            ['المثلثيه', 'المثلثية'],
            ['اللاحقه', 'اللاحقة'],
        ]
        try:
            inputVar = str(inputVar)
            errorCount = 0
            sentenceSplitter = araby.tokenize(inputVar)

            correctCount = len(sentenceSplitter)
            lenOfsentence = len(sentenceSplitter)
            words = []
            for n, s in enumerate(sentenceSplitter):
                for n2, x in enumerate(targetWords):
                    if str(s) == x[0]:
                        errorCount += 1
                        correctCount -= 1
                        sentenceSplitter[n] = x[1]
                        words.append(x[1])
            return (
                self.convertArrayToStr(sentenceSplitter), errorCount, correctCount, lenOfsentence, words
         )
        except Exception as e:
            print('we have error in ', e)

    def bar(self):
        new, errorCount, correctCount, lenOfsentence, self.words = self.correct(self.line1.text())

        self.line2.setText(new)

        # self.lbl_errors.setText(str(errorCount))

        self.lbl_errors.setText("{}".format(errorCount))
        self.lbl_correct.setText("{}".format(correctCount))
        self.lbl_len.setText("{}".format(lenOfsentence))


    def save_output(self):
        name = QFileDialog.getSaveFileName(self, "Save File", '/', '.docs')
        file = open(name, 'w')
        text = self.words
        file.write(text)
        file.close()


def main():
    app = QApplication(argv)
    window = Main()
    window.show()
    app.exec_()
if __name__ == "__main__":
    main()
