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

        # Initialise main window for the extended mode
        self.setFixedSize(QSize(700, 380))
        self.setWindowTitle("SimpleWeatherApplication - Extended")
        self.setStyleSheet("MainWindow {border-image: url(images/gradient.jpg)}")

        # Store the days of the week in a list
        self.days = ['Monday',
                    'Tuesday',
                    'Wednesday',
                    'Thursday',
                    'Friday',
                    'Saturday',
                    'Sunday']

        # Index order: layout, title, icon, weather
        self.nextDaysWeather = [[], [], [], [], []]

        # Create the basic layout for the initial window, which queries the user
        # for the location which they want to find the weather of
        self.layout = QVBoxLayout()
        self.testLabel = QLabel("Please enter a city and country in the form {City, CountryInitials}")
        self.cityBox = QLineEdit()
        self.layout.addWidget(self.testLabel)
        self.layout.addWidget(self.cityBox)
        self.testLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cityBox.setFixedHeight(40)
        self.cityBox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spacer = QLabel()
        self.layout.addWidget(self.spacer)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        # Once the user presses enter/return, after entering their city and country,
        # we call the appropriate method for the next step.
        self.cityBox.returnPressed.connect(self.cityEntered)

    # Use a method that will update the GUI with appropriate information once
    # the user has entered their desired location.
    def cityEntered(self):
        # Fetch the city which the user has just entered, use this to search for
        # the appropriate weather.
        self.cityName = self.cityBox.text() 
        self.cityBox.clear() # Don't need to clear the box but will anyway
        self.delWidget(self.testLabel, self.layout)
        self.delWidget(self.cityBox, self.layout)

        # Create the layouts for the new/updated GUI
        self.currWeatherLayout = QVBoxLayout()
        self.nextWeatherLayout = QHBoxLayout()

        # By default we simply have a label alerting the user that their given
        # location was not found, asking them to try again. This occurs if the
        # location could not be determined by the OpenWeatherMap API.
        self.cityNameLabel = QLabel("The given location was not found, please try again!")
        self.cityNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currWeatherLayout.addWidget(self.cityNameLabel)

        # Use two labels, one for an icon corresponding to the current weather 
        # and one for basic weather information.
        self.weatherIcon = QLabel()
        self.weatherIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currWeatherLayout.addWidget(self.weatherIcon)

        self.currentWeather = QLabel()
        self.currentWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currWeatherLayout.addWidget(self.currentWeather)

        # Create a number of widgets and layouts, each corresponding to a day of
        # the week. Currently I am displaying the next five (5) days of weather
        # supplied by the API.
        for i in range(0,5):
            self.nextDaysWeather[i].append(QVBoxLayout())
            self.nextDaysWeather[i].append(QLabel()) 
            self.nextDaysWeather[i].append(QLabel()) # icon
            self.nextDaysWeather[i].append(QLabel()) 
            self.nextDaysWeather[i][0].addWidget(self.nextDaysWeather[i][1])
            self.nextDaysWeather[i][0].addWidget(self.nextDaysWeather[i][2])
            self.nextDaysWeather[i][0].addWidget(self.nextDaysWeather[i][3])
            self.nextWeatherLayout.addLayout(self.nextDaysWeather[i][0])

        # Align each layout.
        for i in range(0,5):
            for j in range(1,4):
                self.nextDaysWeather[i][j].setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the current weather layout and next weather layout to the main
        # GUI window layout itelf.
        self.layout.addLayout(self.currWeatherLayout)
        self.layout.addLayout(self.nextWeatherLayout)
        
        # Normalise the entry by the user, such that it is in the form City,CountryInitials
        self.cityName.replace(" ", "") # Remove whitespaces
        self.cityName.lower() # Lowercase
        # Be sure to use a try-except block, as an exception will be thrown if
        # the entered location could not be found. This is a simple KeyError
        # due to an invalid JSON object.
        try:
            # Perform an initial update
            self.updateWeather(self.cityName)
        except:
            # Simply pass if the KeyError occurred, we handle this by simply NOT
            # updating the GUI.
            pass

    # A basic function for deleting a QWidget. This is simply a helper function
    # for this file.
    def delWidget(self, widget, layout):
        try:
            layout.removeWidget(widget)
            widget.deleteLater()
            widget = None
        except:
            traceback.print_exc()

    # The main update function is very similar to the basic mode, except now we
    # are simply querying on the fly.
    def updateWeather(self, location):
        # Use the datetime library to get the current day time, such that we 
        # display the appropriate future days.
        curDayNum = datetime.datetime.today().weekday()

        # Now we simply `build` the correct URL to fetch data from the API. Use
        # the basic api call for the forecast method.
        api = "http://api.openweathermap.org/data/2.5/forecast?q="

        # Store the user entered location into an alias
        loc = location

        # Note that we require a VALID api key to be able to query this. Obviously
        # I have left this blank for security purposes, as I do not want my API
        # key being abused.
        apiKey = "enter api key here"

        # Finally ensure we use metric units.
        units = "&units=metric"

        # Build the url from all of this information
        url = api + loc + "&appid=" + apiKey + units

        # Again use requests to fetch the content string from this URL
        request = requests.get(url)

        # Use the json library to parse the json string into a json object
        jsonContent = json.loads(request.content)        

        # Directly fetch the location name from the json object itself
        self.cityNameLabel.setText(jsonContent['city']['name'] + ", " 
        + jsonContent['city']['country'])

        # Now loop 6 times, once for the current weather and once for each of the
        # 5 future weather forecasts. Each time we simply update the appropriate
        # QWidgets corresponding to a specific day. For this we simply make use
        # of our nextDaysWeather 2D list.
        for i in range(6):
            nextDayNum = curDayNum + i# only need this for cur day, OWM records for all days (def val)
            minTemp = jsonContent['list'][i]['main']['temp_min']
            maxTemp = jsonContent['list'][i]['main']['temp_max']
            # Use the api's own codes for icon ID's to set appropriate icon
            icon = jsonContent['list'][i]['weather'][0]['icon']
            if (i == 0):
                # Note that we only require the current temperature and feels
                # like temperature for the current day.
                curTemp = jsonContent['list'][i]['main']['temp'] 
                feelsTemp = jsonContent['list'][i]['main']['feels_like'] 
                self.weatherIcon.setPixmap(QPixmap("images/weather_icons/" + icon + ".png"))
                self.currentWeather.setText(str(minTemp) + "\t\t\t\t" +  str(maxTemp) 
                + "\n\n" + "Currently: " + str(curTemp) + "\n" + "Feels like: " + str(feelsTemp) + "\n")
            else:
                if (nextDayNum > 6):
                    self.nextDaysWeather[i-1][1].setText(self.days[nextDayNum - 7])
                else:
                    self.nextDaysWeather[i-1][1].setText(self.days[nextDayNum])
                self.nextDaysWeather[i-1][2].setPixmap(QPixmap("images/weather_icons/" + icon + ".png"))
                self.nextDaysWeather[i-1][3].setText(str(minTemp) + "\t\t\t\t" + str(maxTemp))