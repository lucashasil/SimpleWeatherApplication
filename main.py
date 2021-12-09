from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import sys
import json
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(1000, 800))
        self.setWindowTitle("My Weather Application")


        self.baseLayout = QGridLayout() # base grid of all locations

        # create separate vertical box layout for each location which will be 
        # put in the grid individually
        self.canLayout = QVBoxLayout()
        self.sydLayout = QVBoxLayout()
        self.darLayout = QVBoxLayout()
        self.briLayout = QVBoxLayout()
        self.adeLayout = QVBoxLayout()
        self.hobLayout = QVBoxLayout()
        self.melLayout = QVBoxLayout()
        self.perLayout = QVBoxLayout()


        self.canLabel = QLabel("Canberra")
        self.sydLabel = QLabel("Sydney")
        self.darLabel = QLabel("Darwin")
        self.briLabel = QLabel("Brisbane")
        self.adeLabel = QLabel("Adelaide")
        self.hobLabel = QLabel("Hobart")
        self.melLabel = QLabel("Melbourne")
        self.perLabel = QLabel("Perth")


        self.canLabelImg = QLabel()
        self.sydLabelImg = QLabel()
        self.darLabelImg = QLabel()
        self.briLabelImg = QLabel()
        self.adeLabelImg = QLabel()
        self.hobLabelImg = QLabel()
        self.melLabelImg = QLabel()
        self.perLabelImg = QLabel()


        self.canLabelWeather = QLabel()
        self.sydLabelWeather = QLabel()
        self.darLabelWeather = QLabel()
        self.briLabelWeather = QLabel()
        self.adeLabelWeather = QLabel()
        self.hobLabelWeather = QLabel()
        self.melLabelWeather = QLabel()
        self.perLabelWeather = QLabel()


        self.canLabelWeather.setText(self.fetchWeather("can"))
        self.sydLabelWeather.setText(self.fetchWeather("syd"))
        self.darLabelWeather.setText(self.fetchWeather("dar"))
        self.briLabelWeather.setText(self.fetchWeather("bri"))
        self.adeLabelWeather.setText(self.fetchWeather("ade"))
        self.hobLabelWeather.setText(self.fetchWeather("hob"))
        self.melLabelWeather.setText(self.fetchWeather("mel"))
        self.perLabelWeather.setText(self.fetchWeather("per"))


        self.canLabelImg.setScaledContents(True)
        self.sydLabelImg.setScaledContents(True)
        self.darLabelImg.setScaledContents(True)
        self.briLabelImg.setScaledContents(True)
        self.adeLabelImg.setScaledContents(True)
        self.hobLabelImg.setScaledContents(True)
        self.melLabelImg.setScaledContents(True)
        self.perLabelImg.setScaledContents(True)

    
        self.canLabelImg.setPixmap(QPixmap('test.jpg'))
        self.sydLabelImg.setPixmap(QPixmap('test.jpg'))
        self.darLabelImg.setPixmap(QPixmap('test.jpg'))
        self.briLabelImg.setPixmap(QPixmap('test.jpg'))
        self.adeLabelImg.setPixmap(QPixmap('test.jpg'))
        self.hobLabelImg.setPixmap(QPixmap('test.jpg'))
        self.melLabelImg.setPixmap(QPixmap('test.jpg'))
        self.perLabelImg.setPixmap(QPixmap('test.jpg'))


        self.canLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.sydLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.darLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.briLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.hobLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.melLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.perLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        self.canLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sydLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.darLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.briLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adeLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hobLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.melLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.perLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.canLabel.setStyleSheet("font-weight: bold; text-decoration: underline;")
        self.sydLabel.setStyleSheet("font-weight: bold; text-decoration: underline;")
        self.darLabel.setStyleSheet("font-weight: bold; text-decoration: underline;")
        self.briLabel.setStyleSheet("font-weight: bold; text-decoration: underline;")
        self.adeLabel.setStyleSheet("font-weight: bold; text-decoration: underline;")
        self.hobLabel.setStyleSheet("font-weight: bold; text-decoration: underline;")
        self.melLabel.setStyleSheet("font-weight: bold; text-decoration: underline;")
        self.perLabel.setStyleSheet("font-weight: bold; text-decoration: underline;")

        self.canLabelWeather.setStyleSheet("border: 1.3px solid black;")
        self.sydLabelWeather.setStyleSheet("border: 1.3px solid black;")
        self.darLabelWeather.setStyleSheet("border: 1.3px solid black;")
        self.briLabelWeather.setStyleSheet("border: 1.3px solid black;")
        self.adeLabelWeather.setStyleSheet("border: 1.3px solid black;")
        self.hobLabelWeather.setStyleSheet("border: 1.3px solid black;")
        self.melLabelWeather.setStyleSheet("border: 1.3px solid black;")
        self.perLabelWeather.setStyleSheet("border: 1.3px solid black;")

        self.canLayout.addWidget(self.canLabel)
        self.sydLayout.addWidget(self.sydLabel)
        self.darLayout.addWidget(self.darLabel)
        self.briLayout.addWidget(self.briLabel)
        self.adeLayout.addWidget(self.adeLabel)
        self.hobLayout.addWidget(self.hobLabel)
        self.melLayout.addWidget(self.melLabel)
        self.perLayout.addWidget(self.perLabel)


        self.canLayout.addWidget(self.canLabelImg)
        self.sydLayout.addWidget(self.sydLabelImg)
        self.darLayout.addWidget(self.darLabelImg)
        self.briLayout.addWidget(self.briLabelImg)
        self.adeLayout.addWidget(self.adeLabelImg)
        self.hobLayout.addWidget(self.hobLabelImg)
        self.melLayout.addWidget(self.melLabelImg)
        self.perLayout.addWidget(self.perLabelImg)


        self.canLayout.addWidget(self.canLabelWeather)
        self.sydLayout.addWidget(self.sydLabelWeather)
        self.darLayout.addWidget(self.darLabelWeather)
        self.briLayout.addWidget(self.briLabelWeather)
        self.adeLayout.addWidget(self.adeLabelWeather)
        self.hobLayout.addWidget(self.hobLabelWeather)
        self.melLayout.addWidget(self.melLabelWeather)
        self.perLayout.addWidget(self.perLabelWeather)


        self.baseLayout.addLayout(self.canLayout, 0, 0)
        self.baseLayout.addLayout(self.sydLayout, 0, 1)
        self.baseLayout.addLayout(self.darLayout, 0, 2)
        self.baseLayout.addLayout(self.briLayout, 1, 0)
        self.baseLayout.addLayout(self.adeLayout, 1, 1)
        self.baseLayout.addLayout(self.hobLayout, 1, 2)
        self.baseLayout.addLayout(self.melLayout, 2, 0)
        self.baseLayout.addLayout(self.perLayout, 2, 2)


        self.widget = QWidget() # base widget
        self.widget.setLayout(self.baseLayout)
        self.setCentralWidget(self.widget)

        self.timer = QTimer(self)
        self.timer.setInterval(300000) # 5 minute intervals
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.updateWeather)
        self.timer.start(300000) # 5 minute intervals


    def fetchWeather(self, location):
        match location:
            case "can":
                url = "http://www.bom.gov.au/fwo/IDN60903/IDN60903.94926.json"
            case "syd":
                url = "http://www.bom.gov.au/fwo/IDN60901/IDN60901.95766.json"
            case "dar":
                url = "http://www.bom.gov.au/fwo/IDD60901/IDD60901.95122.json"
            case "bri":
                url = "http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.json"
            case "ade":
                url = "http://www.bom.gov.au/fwo/IDS60901/IDS60901.94672.json"
            case "hob":
                url = "http://www.bom.gov.au/fwo/IDT60901/IDT60901.94970.json"
            case "mel":
                url = "http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json"
            case "per":
                url = "http://www.bom.gov.au/fwo/IDW60901/IDW60901.94608.json"

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

        return ("Station location: " + statLoc + "\n"
        + "Local Time: " + locTime[3:len(locTime)] + "\n"
        + "Temperature: " + temp + u"\N{DEGREE SIGN}" + "C" + "\n"
        + "Humidity: " + hum)

    def updateWeather(self):
        self.canLabelWeather.setText(self.fetchWeather("can"))
        self.sydLabelWeather.setText(self.fetchWeather("syd"))
        self.darLabelWeather.setText(self.fetchWeather("dar"))
        self.briLabelWeather.setText(self.fetchWeather("bri"))
        self.adeLabelWeather.setText(self.fetchWeather("ade"))
        self.hobLabelWeather.setText(self.fetchWeather("hob"))
        self.melLabelWeather.setText(self.fetchWeather("mel"))
        self.perLabelWeather.setText(self.fetchWeather("per"))
        print("updated")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()