from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys
import json
import requests
#from requests.api import request

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(1000, 600))
        self.setWindowTitle("My Weather Application")
        
        baseLayout = QGridLayout() # base grid of all locations

        # create separate vertical box layout for each location which will be 
        # put in the grid individually
        canLayout = QVBoxLayout()
        sydLayout = QVBoxLayout()
        darLayout = QVBoxLayout()
        briLayout = QVBoxLayout()
        adeLayout = QVBoxLayout()
        hobLayout = QVBoxLayout()
        melLayout = QVBoxLayout()
        perLayout = QVBoxLayout()


        canLabel = QLabel("Canberra")
        sydLabel = QLabel("Sydney")
        darLabel = QLabel("Darwin")
        briLabel = QLabel("Brisbane")
        adeLabel = QLabel("Adelaide")
        hobLabel = QLabel("Hobart")
        melLabel = QLabel("Melbourne")
        perLabel = QLabel("Perth")


        canLabelImg = QLabel()
        sydLabelImg = QLabel()
        darLabelImg = QLabel()
        briLabelImg = QLabel()
        adeLabelImg = QLabel()
        hobLabelImg = QLabel()
        melLabelImg = QLabel()
        perLabelImg = QLabel()


        canLabelWeather = QLabel()
        sydLabelWeather = QLabel()
        darLabelWeather = QLabel()
        briLabelWeather = QLabel()
        adeLabelWeather = QLabel()
        hobLabelWeather = QLabel()
        melLabelWeather = QLabel()
        perLabelWeather = QLabel()


        canLabelWeather.setText(self.fetchWeather("can"))
        sydLabelWeather.setText(self.fetchWeather("syd"))
        darLabelWeather.setText(self.fetchWeather("dar"))
        briLabelWeather.setText(self.fetchWeather("bri"))
        adeLabelWeather.setText(self.fetchWeather("ade"))
        hobLabelWeather.setText(self.fetchWeather("hob"))
        melLabelWeather.setText(self.fetchWeather("mel"))
        perLabelWeather.setText(self.fetchWeather("per"))


        canLabelImg.setScaledContents(True)
        sydLabelImg.setScaledContents(True)
        darLabelImg.setScaledContents(True)
        briLabelImg.setScaledContents(True)
        adeLabelImg.setScaledContents(True)
        hobLabelImg.setScaledContents(True)
        melLabelImg.setScaledContents(True)
        perLabelImg.setScaledContents(True)

    
        canLabelImg.setPixmap(QPixmap('test.jpg'))
        sydLabelImg.setPixmap(QPixmap('test.jpg'))
        darLabelImg.setPixmap(QPixmap('test.jpg'))
        briLabelImg.setPixmap(QPixmap('test.jpg'))
        adeLabelImg.setPixmap(QPixmap('test.jpg'))
        hobLabelImg.setPixmap(QPixmap('test.jpg'))
        melLabelImg.setPixmap(QPixmap('test.jpg'))
        perLabelImg.setPixmap(QPixmap('test.jpg'))


        canLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        sydLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        darLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        briLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        adeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        hobLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        melLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        perLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        canLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sydLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        darLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        briLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        adeLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hobLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        melLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)
        perLabelWeather.setAlignment(Qt.AlignmentFlag.AlignCenter)

        canLayout.addWidget(canLabel)
        sydLayout.addWidget(sydLabel)
        darLayout.addWidget(darLabel)
        briLayout.addWidget(briLabel)
        adeLayout.addWidget(adeLabel)
        hobLayout.addWidget(hobLabel)
        melLayout.addWidget(melLabel)
        perLayout.addWidget(perLabel)


        canLayout.addWidget(canLabelImg)
        sydLayout.addWidget(sydLabelImg)
        darLayout.addWidget(darLabelImg)
        briLayout.addWidget(briLabelImg)
        adeLayout.addWidget(adeLabelImg)
        hobLayout.addWidget(hobLabelImg)
        melLayout.addWidget(melLabelImg)
        perLayout.addWidget(perLabelImg)


        canLayout.addWidget(canLabelWeather)
        sydLayout.addWidget(sydLabelWeather)
        darLayout.addWidget(darLabelWeather)
        briLayout.addWidget(briLabelWeather)
        adeLayout.addWidget(adeLabelWeather)
        hobLayout.addWidget(hobLabelWeather)
        melLayout.addWidget(melLabelWeather)
        perLayout.addWidget(perLabelWeather)


        baseLayout.addLayout(canLayout, 0, 0)
        baseLayout.addLayout(sydLayout, 0, 1)
        baseLayout.addLayout(darLayout, 0, 2)
        baseLayout.addLayout(briLayout, 1, 0)
        baseLayout.addLayout(adeLayout, 1, 1)
        baseLayout.addLayout(hobLayout, 1, 2)
        baseLayout.addLayout(melLayout, 2, 0)
        baseLayout.addLayout(perLayout, 2, 2)


        widget = QWidget() # base widget
        widget.setLayout(baseLayout)
        self.setCentralWidget(widget)


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
        # print(jsonContent['observations']['data'][0]['name']) # this is index for station location
        # print(jsonContent['observations']['data'][0]["local_date_time"])
        # print(jsonContent['observations']['data'][0]["air_temp"]) # 0 is the most recent weather report
        # if (jsonContent['observations']['data'][0]["cloud"] == "-"):
        #     print("Clear")
        # else:
        #     print(jsonContent['observations']['data'][0]["cloud"])
        # print(str(jsonContent['observations']['data'][0]["rel_hum"]) + '%')
        return (jsonContent['observations']['data'][0]['name'] + " " + jsonContent['observations']['data'][0]["local_date_time"] + " " + str(jsonContent['observations']['data'][0]["air_temp"]) + " " + str(jsonContent['observations']['data'][0]["rel_hum"]) + "%")


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
