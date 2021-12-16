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


        self.nextDaysWeather = [[], [], [], [], []]


        self.layout = QVBoxLayout()
        self.testLabel = QLabel("testing")
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
        self.cityName = self.cityBox.text()
        self.cityBox.clear() # don't really need to clear the box if we are transitioning to a new GUI anyway
        self.delWidget(self.testLabel, self.layout)
        self.delWidget(self.cityBox, self.layout)


        self.currWeatherLayout = QVBoxLayout()
        self.nextWeatherLayout = QHBoxLayout()


        for i in range(0,5):
            self.nextDaysWeather[i].append(QVBoxLayout())
            self.nextDaysWeather[i].append(QLabel("Next day name"))
            self.nextDaysWeather[i].append(QLabel())
            self.nextDaysWeather[i].append(QLabel("Next weather"))
            self.nextDaysWeather[i][0].addWidget(self.nextDaysWeather[i][1])
            self.nextDaysWeather[i][0].addWidget(self.nextDaysWeather[i][2])
            self.nextDaysWeather[i][0].addWidget(self.nextDaysWeather[i][3])
            self.nextWeatherLayout.addLayout(self.nextDaysWeather[i][0])


        for i in range(0,5):
            for j in range(1,4):
                self.nextDaysWeather[i][j].setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.cityNameLabel = QLabel(self.cityName)
        self.cityNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currWeatherLayout.addWidget(self.cityNameLabel)

        self.weatherIcon = QLabel()
        self.weatherIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currWeatherLayout.addWidget(self.weatherIcon)


        self.currentWeather = QLabel(self.fetchWeather("Melbourne,au", 0))
        self.currentWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currWeatherLayout.addWidget(self.currentWeather)


        self.layout.addLayout(self.currWeatherLayout)
        self.layout.addLayout(self.nextWeatherLayout)


    def delWidget(self, widget, layout): # technically QLineEdit inherits QFrame NOT QWidget
        try:
            layout.removeWidget(widget)
            widget.deleteLater()
            widget = None
        except:
            traceback.print_exc()


    def fetchWeather(self, location, day): # use 0 for current day, 1, 2, etc for nexts
        api = "http://api.openweathermap.org/data/2.5/forecast?q="
        loc = location
        apiKey = "6e22f5d788993623bc42245d9efbb85d" # todo change this to not be uploaded to github
        units = "&units=metric"
        url = api + loc + "&appid=" + apiKey + units

        request = requests.get(url)
        jsonContent = json.loads(request.content)
        curTemp = jsonContent['list'][day]['main']['temp']
        feelsTemp = jsonContent['list'][day]['main']['feels_like']
        minTemp = jsonContent['list'][day]['main']['temp_min']
        maxTemp = jsonContent['list'][day]['main']['temp_max']
        icon = jsonContent['list'][day]['weather'][0]['icon']
        self.weatherIcon.setPixmap(QPixmap("images/weather_icons/" + icon + ".png"))
        for i in range(1,6):
            nextMin = str(jsonContent['list'][i]['main']['temp_min'])
            nextMax = str(jsonContent['list'][i]['main']['temp_max'])
            nextIcon = jsonContent['list'][i]['weather'][0]['icon']
            self.nextDaysWeather[i-1][2].setPixmap(QPixmap("images/weather_icons/" + nextIcon + ".png"))
            self.nextDaysWeather[i-1][3].setText(nextMin + "\t\t\t\t" + nextMax)
        return ("Current tempereature: " + str(curTemp) + "\n" + "Feels like: " + str(feelsTemp) + "\n" + "Min: " + str(minTemp) + "\n" + "Max: " +  str(maxTemp))


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
