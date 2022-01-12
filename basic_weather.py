from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import json
import requests
import time

class MainWindow(QMainWindow):

    # Store a list of each capital city of Australia
    cities = ["Adelaide", "Brisbane", "Canberra", "Darwin", "Hobart"
             , "Melbourne", "Perth", "Sydney"]

    def __init__(self):
        super().__init__()

        # Initialise the window for this mode
        self.setFixedSize(QSize(1000, 700))
        self.setWindowTitle("SimpleWeatherApplication - Basic")

        # Use a grid based layout for this mode
        self.baseLayout = QGridLayout()

        # Iterate over every capital city and create new QWidgets for each 
        # appropriate item for EACH capital city, appending each QWidget to
        # a sublist of this 2D list.
        self.citiesList = []

        for i in range(len(self.cities)):
            self.citiesList.append([])

        # Add the layouts and their respective widgets to their own lists
        for i in range(len(self.cities)):
            self.citiesList[i].append(QVBoxLayout())
            self.citiesList[i].append(QLabel(self.cities[i]))
            self.citiesList[i].append(QLabel())
            self.citiesList[i][2].setPixmap(QPixmap("images/" + self.cities[i] + ".jpg"))
            self.citiesList[i].append(QLabel(self.fetchWeather(self.cities[i])))

        # Add the widgets to their correct layouts
        for i in range(len(self.citiesList)):
            for j in range(1, len(self.citiesList[i])):
                self.citiesList[i][2].setScaledContents(True)
                self.citiesList[i][1].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.citiesList[i][1].setStyleSheet("font-weight: bold; text-decoration: underline;")
                self.citiesList[i][3].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.citiesList[i][3].setStyleSheet("border: 1.3px solid black;")
                self.citiesList[i][0].addWidget(self.citiesList[i][j])

        # Create a final layout which acts as a basic information widget which
        # will take up the final grid spot. This will simply display the last
        # time the application had attempted to update the weather information.
        self.infoLayout = QVBoxLayout()
        self.lastUpdate = QLabel(self.updateTime()) # Use the correct method
        self.lastUpdate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.infoLayout.addWidget(self.lastUpdate)

        # Add each city and it's layout to the base layout of the window itself
        self.baseLayout.addLayout(self.citiesList[0][0], 0, 0)
        self.baseLayout.addLayout(self.citiesList[1][0], 0, 1)
        self.baseLayout.addLayout(self.citiesList[2][0], 0, 2)
        self.baseLayout.addLayout(self.citiesList[3][0], 1, 0)
        self.baseLayout.addLayout(self.citiesList[4][0], 1, 1)
        self.baseLayout.addLayout(self.citiesList[5][0], 1, 2)
        self.baseLayout.addLayout(self.citiesList[6][0], 2, 0)
        self.baseLayout.addLayout(self.infoLayout, 2, 1)
        self.baseLayout.addLayout(self.citiesList[7][0], 2, 2)

        # Use a dummy widget and set it's layout to the main layout
        self.widget = QWidget() # base widget
        self.widget.setLayout(self.baseLayout)
        self.setCentralWidget(self.widget)

        # Setup a basic timer (a QTimer) and set it to call the updateWeather
        # method every 5 minutes.
        self.timer = QTimer(self)
        self.timer.setInterval(300000)
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.updateWeather)
        self.timer.start(300000)

    # The basic method for fetching weather from the BOM database
    def fetchWeather(self, location):
        # Note this requires Python 3.10+ due to the match statement. Each of 
        # the following JSON files can be found easily via a quick search on
        # the BOM website. If these change in the future this application will
        # break.
        match location:
            case "Canberra":
                url = "http://www.bom.gov.au/fwo/IDN60903/IDN60903.94926.json"
            case "Sydney":
                url = "http://www.bom.gov.au/fwo/IDN60901/IDN60901.95765.json"
            case "Darwin":
                url = "http://www.bom.gov.au/fwo/IDD60901/IDD60901.94120.json"
            case "Brisbane":
                url = "http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.json"
            case "Adelaide":
                url = "http://www.bom.gov.au/fwo/IDS60901/IDS60901.94672.json"
            case "Hobart":
                url = "http://www.bom.gov.au/fwo/IDT60901/IDT60901.94970.json"
            case "Melbourne":
                url = "http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json"
            case "Perth":
                url = "http://www.bom.gov.au/fwo/IDW60901/IDW60901.94608.json"

        # We need to use the appropriate headers when fetching content such that
        # the url will not reject the request. The following headers correspond
        # to a Firefox browser.
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

        # Use requests with the correct headers to fetch the content string
        request = requests.get(url, headers=headers)

        # Convert this string to a JSON object using the json library
        jsonContent = json.loads(request.content)

        # Access the relevant weather data by simply accessing the json object
        # directly. See the above links for a specific breakdown of the files
        # indices.
        statLoc = jsonContent['observations']['data'][0]['name']
        locTime = jsonContent['observations']['data'][0]["local_date_time"]
        temp = str(jsonContent['observations']['data'][0]["air_temp"])
        humPer = str(jsonContent['observations']['data'][0]["rel_hum"])
        if (humPer == "None"):
            hum = "0%"
        else:
            hum = humPer + "%"
        # Return all of this information as a single string.
        return ("Station Location: " + statLoc + "\n"
        + "Last Update (Local Time): " + locTime[3:len(locTime)] + "\n"
        + "Temperature: " + temp + u"\N{DEGREE SIGN}" + "C" + "\n"
        + "Humidity: " + hum)

    # Every 5 minutes we call the following method which simply sets the weather
    # for each city again, acting as an update.
    def updateWeather(self):
        for i in range(len(self.citiesList)):
            self.citiesList[i][3].setText(self.fetchWeather(self.cities[i]))
        self.lastUpdate.setText(self.updateTime())
   
    # We also need to update the time which we last updated the weatherm, for
    # this we simply use the time library.
    def updateTime(self):
        t = time.localtime()
        curTime = time.strftime("%I:%M%p", t).lower()
        return ("Last Update: " + curTime)