from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import json
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(1000, 700))
        self.setWindowTitle("SimpleWeatherApplication")

        self.testLabel = QLabel(self.fetchWeather("Melbourne,au"))

        # self.widget = QWidget()
        self.setCentralWidget(self.testLabel)



    def fetchWeather(self, location):
        api = "http://api.openweathermap.org/data/2.5/weather?q="
        loc = location
        apiKey = "6e22f5d788993623bc42245d9efbb85d" #todo change this to not be uploaded to github
        units = "&units=metric"
        url = api + loc + "&appid=" + apiKey + units

        request = requests.get(url)
        jsonContent = json.loads(request.content)
        # return json.loads(request.content)
        return (str(jsonContent["main"]["temp"]))

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
