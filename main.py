import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtGui import QFont, QFontDatabase

class Digital_Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 250, 850, 200)

        font_id = QFontDatabase.addApplicationFont('DS-DIGII.ttf')
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 160)

        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        
        self.timer_label = QLabel("12:00:00 AM", self)
        self.timer_label.setGeometry(0, 0, 850, 200)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet( 'font-size: 170px;'
                                        'color: white;')
        self.timer_label.setFont(my_font)
        
        self.setStyleSheet('background-color: black;')

        self.update_time()

    def update_time(self):
        self.time = QTime.currentTime().toString('hh:mm:ss AP')
        self.timer_label.setText(self.time)
        self.timer.start(1000)

def main():
    app = QApplication(sys.argv)
    clock = Digital_Clock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()