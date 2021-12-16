from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import json
import requests
import traceback

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(700, 350))
        self.setWindowTitle("SimpleWeatherApplication")
        self.setStyleSheet("MainWindow {border-image: url(images/gradient.jpg)}")


        self.layout = QVBoxLayout()
        self.testLabel = QLabel(self.fetchWeather("Melbourne,au"))
        self.cityBox = QLineEdit()
        self.layout.addWidget(self.testLabel)
        self.layout.addWidget(self.cityBox)
        self.testLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cityBox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.cityBox.returnPressed.connect(self.cityEntered)

        # update GUI once city entered


    def cityEntered(self):
        cityName = self.cityBox.text()
        self.cityBox.clear() # don't really need to clear the box if we are transitioning to a new GUI anyway
        print(cityName)
        self.delWidget(self.testLabel, self.layout)
        self.delWidget(self.cityBox, self.layout)
        self.cityLabel = QLabel("City label")
        self.cityLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currentWeather = QLabel("City weather")
        self.currentWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nextWeather = QLabel("Upcoming weather")
        self.nextWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.cityLabel)
        self.layout.addWidget(self.currentWeather)
        self.layout.addWidget(self.nextWeather)


        # add images for specific weather here, show next few days


    def delWidget(self, widget, layout): # technically QLineEdit inherits QFrame NOT QWidget
        try:
            layout.removeWidget(widget)
            widget.deleteLater()
            widget = None
        except:
            traceback.print_exc()


    def fetchWeather(self, location):
        api = "http://api.openweathermap.org/data/2.5/weather?q="
        loc = location
        apiKey = "enter api key here" #todo change this to not be uploaded to github
        units = "&units=metric"
        url = api + loc + "&appid=" + apiKey + units

        request = requests.get(url)
        jsonContent = json.loads(request.content)
        # return (str(jsonContent["main"]["temp"]))
        return "testing"


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
