from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import basic_weather as bw
import extended_weather as ew
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Setup initial window
        self.setFixedSize(QSize(800, 500))
        self.setWindowTitle("SimpleWeatherApplication")
        self.setStyleSheet("MainWindow {border-image: url(images/gradient.jpg)}")

        # Setup main layouts for the window itself and appropriate QWidgets
        self.mainLayout = QVBoxLayout()
        self.subLayout = QHBoxLayout()

        self.choiceLabel = QLabel("Please select which mode you would like to run:")
        self.choiceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.choiceLabel)
        
        # Add a button for each basic and extended modes
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

        # Create a dummy widget and set it's layout manager to the main layout
        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

        # Connect each button to it's appropriate method
        self.basicMode.clicked.connect(self.newBasicWindow)
        self.extendedMode.clicked.connect(self.newExtendWindow)

    # Create basic methods for the basic and extended modes. These methods 
    # simply create a new window corresponding to the appropriate mode, whilst
    # also hiding the initial window and showing the new window.
    def newBasicWindow(self):
        self.bW = bw.MainWindow()
        self.bW.show()
        self.hide()

    def newExtendWindow(self):
        self.eW = ew.MainWindow()
        self.eW.show()
        self.hide()

# Basic main method which creates a new QApplication and initialises a basic
# main/initial window.
def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# Ensure application is being run from THIS file
if __name__ == "__main__":
    main()