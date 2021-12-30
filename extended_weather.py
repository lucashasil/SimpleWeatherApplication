from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import datetime
import json
import requests
import traceback

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(700, 350))
        self.setWindowTitle("SimpleWeatherApplication")
        self.setStyleSheet("MainWindow {border-image: url(images/gradient.jpg)}")

        self.days = ['Monday',
                    'Tuesday',
                    'Wednesday',
                    'Thursday',
                    'Friday',
                    'Saturday',
                    'Sunday']

        # index order: layout, title, icon, weather
        self.nextDaysWeather = [[], [], [], [], []]


        self.layout = QVBoxLayout()
        self.testLabel = QLabel("What city would you like a forecast for? (Enter as: City,CountryInitials)")
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
        self.cityName = self.cityBox.text() # keep the name entered in the box
        self.cityBox.clear() # don't really need to clear the box if we are transitioning to a new GUI anyway
        self.delWidget(self.testLabel, self.layout)
        self.delWidget(self.cityBox, self.layout)


        self.currWeatherLayout = QVBoxLayout()
        self.nextWeatherLayout = QHBoxLayout()


        self.cityNameLabel = QLabel()
        self.cityNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currWeatherLayout.addWidget(self.cityNameLabel)


        self.weatherIcon = QLabel()
        self.weatherIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currWeatherLayout.addWidget(self.weatherIcon)


        self.currentWeather = QLabel()
        self.currentWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currWeatherLayout.addWidget(self.currentWeather)


        for i in range(0,5):
            self.nextDaysWeather[i].append(QVBoxLayout())
            self.nextDaysWeather[i].append(QLabel("DEF_NAME")) 
            self.nextDaysWeather[i].append(QLabel()) # icon
            self.nextDaysWeather[i].append(QLabel("DEF_WEATHER")) 
            self.nextDaysWeather[i][0].addWidget(self.nextDaysWeather[i][1])
            self.nextDaysWeather[i][0].addWidget(self.nextDaysWeather[i][2])
            self.nextDaysWeather[i][0].addWidget(self.nextDaysWeather[i][3])
            self.nextWeatherLayout.addLayout(self.nextDaysWeather[i][0])


        for i in range(0,5):
            for j in range(1,4):
                self.nextDaysWeather[i][j].setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addLayout(self.currWeatherLayout)
        self.layout.addLayout(self.nextWeatherLayout)
        
        # update weather once initially
        self.updateWeather(self.cityName)


    def delWidget(self, widget, layout): # technically QLineEdit inherits QFrame NOT QWidget
        try:
            layout.removeWidget(widget)
            widget.deleteLater()
            widget = None
        except:
            traceback.print_exc()


    def updateWeather(self, location): # use 0 for current day, 1, 2, etc for nexts
        curDayNum = datetime.datetime.today().weekday()
        api = "http://api.openweathermap.org/data/2.5/forecast?q="
        loc = location
        apiKey = "enter api key here" # todo change this to not be uploaded to github
        units = "&units=metric"
        url = api + loc + "&appid=" + apiKey + units
        request = requests.get(url)
        jsonContent = json.loads(request.content)
        self.cityNameLabel.setText(jsonContent['city']['name'] + ", " + jsonContent['city']['country'])
        for i in range(6):
            nextDayNum = curDayNum + i
            curTemp = jsonContent['list'][i]['main']['temp'] # only need this for cur day, OWM records for all days (def val)
            feelsTemp = jsonContent['list'][i]['main']['feels_like'] # only need this for cur day, OWM records for all days (def val)
            minTemp = jsonContent['list'][i]['main']['temp_min']
            maxTemp = jsonContent['list'][i]['main']['temp_max']
            icon = jsonContent['list'][i]['weather'][0]['icon']
            if (i == 0):
                self.weatherIcon.setPixmap(QPixmap("images/weather_icons/" + icon + ".png"))
                self.currentWeather.setText(str(minTemp) + "\t\t\t\t" +  str(maxTemp) + "\n\n" + "Currently: " + str(curTemp) + "\n" + "Feels like: " + str(feelsTemp))
            else:
                if (nextDayNum > 6):
                    self.nextDaysWeather[i-1][1].setText(self.days[nextDayNum - 7])
                else:
                    self.nextDaysWeather[i-1][1].setText(self.days[nextDayNum])
                self.nextDaysWeather[i-1][2].setPixmap(QPixmap("images/weather_icons/" + icon + ".png"))
                self.nextDaysWeather[i-1][3].setText(str(minTemp) + "\t\t\t\t" + str(maxTemp))


app = QApplication([])
window = MainWindow()
window.show()
app.exec()