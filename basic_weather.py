from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import json
import requests
import time

class MainWindow(QMainWindow):

    cities = ["Adelaide", "Brisbane", "Canberra", "Darwin", "Hobart"
             , "Melbourne", "Perth", "Sydney"]

    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(1000, 700))
        self.setWindowTitle("SimpleWeatherApplication")

        self.baseLayout = QGridLayout() # base grid of all locations

        self.citiesList = []

        for i in range(len(self.cities)):
            self.citiesList.append([])

        # add the layouts and their respective widgets to their own lists
        for i in range(len(self.cities)):
            self.citiesList[i].append(QVBoxLayout())
            self.citiesList[i].append(QLabel(self.cities[i]))
            self.citiesList[i].append(QLabel())
            self.citiesList[i][2].setPixmap(QPixmap("images/" + self.cities[i] + ".jpg"))
            self.citiesList[i].append(QLabel(self.fetchWeather(self.cities[i])))

        # add the widgets to their layouts
        for i in range(len(self.citiesList)):
            for j in range(1, len(self.citiesList[i])):
                self.citiesList[i][2].setScaledContents(True)
                self.citiesList[i][1].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.citiesList[i][1].setStyleSheet("font-weight: bold; text-decoration: underline;")
                self.citiesList[i][3].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.citiesList[i][3].setStyleSheet("border: 1.3px solid black;")
                self.citiesList[i][0].addWidget(self.citiesList[i][j])

        # fill final grid slot with basic information
        self.infoLayout = QVBoxLayout()
        self.lastUpdate = QLabel(self.updateTime())
        self.lastUpdate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.infoLayout.addWidget(self.lastUpdate)


        self.baseLayout.addLayout(self.citiesList[0][0], 0, 0)
        self.baseLayout.addLayout(self.citiesList[1][0], 0, 1)
        self.baseLayout.addLayout(self.citiesList[2][0], 0, 2)
        self.baseLayout.addLayout(self.citiesList[3][0], 1, 0)
        self.baseLayout.addLayout(self.citiesList[4][0], 1, 1)
        self.baseLayout.addLayout(self.citiesList[5][0], 1, 2)
        self.baseLayout.addLayout(self.citiesList[6][0], 2, 0)
        self.baseLayout.addLayout(self.infoLayout, 2, 1)
        self.baseLayout.addLayout(self.citiesList[7][0], 2, 2)


        self.widget = QWidget() # base widget
        self.widget.setLayout(self.baseLayout)
        self.setCentralWidget(self.widget)

        self.timer = QTimer(self)
        self.timer.setInterval(300000) # 5 minute intervals
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.updateWeather)
        self.timer.start(300000) # 5 minute intervals


    def fetchWeather(self, location):
        # match location:
        #     case "Canberra":
        #         url = "http://www.bom.gov.au/fwo/IDN60903/IDN60903.94926.json"
        #     case "Sydney":
        #         url = "http://www.bom.gov.au/fwo/IDN60901/IDN60901.95765.json"
        #     case "Darwin":
        #         url = "http://www.bom.gov.au/fwo/IDD60901/IDD60901.95122.json"
        #     case "Brisbane":
        #         url = "http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.json"
        #     case "Adelaide":
        #         url = "http://www.bom.gov.au/fwo/IDS60901/IDS60901.94672.json"
        #     case "Hobart":
        #         url = "http://www.bom.gov.au/fwo/IDT60901/IDT60901.94970.json"
        #     case "Melbourne":
        #         url = "http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json"
        #     case "Perth":
        #         url = "http://www.bom.gov.au/fwo/IDW60901/IDW60901.94608.json"

        url = "http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'} # needed to authenticate, need user-agnt
        request = requests.get(url, headers=headers)
        jsonContent = json.loads(request.content)
        statLoc = jsonContent['observations']['data'][0]['name']
        locTime = jsonContent['observations']['data'][0]["local_date_time"]
        temp = str(jsonContent['observations']['data'][0]["air_temp"])
        humPer = str(jsonContent['observations']['data'][0]["rel_hum"])
        if (humPer == "None"):
            hum = "0%"
        else:
            hum = humPer + "%"

        return ("Station Location: " + statLoc + "\n"
        + "Last Update (Local Time): " + locTime[3:len(locTime)] + "\n"
        + "Temperature: " + temp + u"\N{DEGREE SIGN}" + "C" + "\n"
        + "Humidity: " + hum)

    def updateWeather(self):
        for i in range(len(self.citiesList)):
            self.citiesList[i][3].setText(self.fetchWeather(self.cities[i]))
        self.lastUpdate.setText(self.updateTime())

    def updateTime(self):
        t = time.localtime()
        curTime = time.strftime("%I:%M%p", t).lower()
        return ("Last Update: " + curTime)


def run():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

# if __name__ == "__main__":
#     main()