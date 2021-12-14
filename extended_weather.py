from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import json
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(700, 350))
        self.setWindowTitle("SimpleWeatherApplication")

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


    def cityEntered(self):
        cityName = self.cityBox.text()
        self.cityBox.clear() # don't really need to clear the box if we are transitioning to a new GUI anyway
        print(cityName)


    def fetchWeather(self, location):
        api = "http://api.openweathermap.org/data/2.5/weather?q="
        loc = location
        apiKey = "enter api key here" #todo change this to not be uploaded to github
        units = "&units=metric"
        url = api + loc + "&appid=" + apiKey + units

        request = requests.get(url)
        jsonContent = json.loads(request.content)
        # return json.loads(request.content)
        # print(url)
        return (str(jsonContent["main"]["temp"]))

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
