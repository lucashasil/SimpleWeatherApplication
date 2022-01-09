from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import basic_weather as bw
import extended_weather as ew
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(800, 500))
        self.setWindowTitle("SimpleWeatherApplication - Extended")
        self.setStyleSheet("MainWindow {border-image: url(images/gradient.jpg)}")


        self.mainLayout = QVBoxLayout()
        self.subLayout = QHBoxLayout()

        self.choiceLabel = QLabel("Please select which mode you would like to run:")
        self.choiceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.choiceLabel)

        self.basicMode = QPushButton("Basic Mode")
        self.basicMode.setFixedHeight(125)
        self.subLayout.addWidget(self.basicMode)

        self.extendedMode = QPushButton("Extended Mode")
        self.extendedMode.setFixedHeight(125)
        self.subLayout.addWidget(self.extendedMode)


        self.mainLayout.addLayout(self.subLayout)

        self.emptyLabel = QLabel()
        self.emptyLabel.setFixedHeight(80)
        self.mainLayout.addWidget(self.emptyLabel)


        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

        # connect buttons to appropriate methods
        self.basicMode.clicked.connect(self.basicWindow)
        self.extendedMode.clicked.connect(self.extendWindow)

    def basicWindow(self):
        self.bW = bw.MainWindow()
        self.bW.show()
        self.hide()

    def extendWindow(self):
        self.eW = ew.MainWindow()
        self.eW.show()
        self.hide()

        
def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()

