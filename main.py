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

        self.setFixedSize(QSize(800, 500))
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

        # testwidget = QLabel("test")
        # testwidget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # canLayout.addWidget(testwidget)

        canLabel = QLabel("Canberra")
        sydLabel = QLabel("Sydney")
        darLabel = QLabel("Darwin")
        briLabel = QLabel("Brisbane")
        adeLabel = QLabel("Adelaide")
        hobLabel = QLabel("Hobart")
        melLabel = QLabel("Melbourne")
        perLabel = QLabel("Perth")

        canLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        sydLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        darLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        briLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        adeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        hobLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        melLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        perLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 


        canLayout.addWidget(canLabel)
        sydLayout.addWidget(sydLabel)
        darLayout.addWidget(darLabel)
        briLayout.addWidget(briLabel)
        adeLayout.addWidget(adeLabel)
        hobLayout.addWidget(hobLabel)
        melLayout.addWidget(melLabel)
        perLayout.addWidget(perLabel)

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



    # def main():
        # window = tk.Tk()
        # window.geometry("800x500")
        # window.title("The Weather")
        # window.grid_rowconfigure(0, weight=1)
        # window.grid_columnconfigure(0, weight=1)
        # window.resizable(0, 0)

        # canLayout = QVBoxLayout()
        # sydLayout = QVBoxLayout()
        # darLayout = QVBoxLayout()
        # briLayout = QVBoxLayout()
        # adeLayout = QVBoxLayout()
        # hobLayout = QVBoxLayout()
        # melLayout = QVBoxLayout()
        # perLayout = QVBoxLayout()

        # canLab = tk.Label(canLayout, text="Canberra").grid(row=0, column=0, padx=10, pady=10)
        # sydLab = tk.Label(sydLayout, text="Sydney").grid(row=0, column=1, padx=10, pady=10)
        # darLab = tk.Label(darLayout, text="Darwin").grid(row=0, column=2, padx=10, pady=10)
        # briLab = tk.Label(briLayout, text="Brisbane").grid(row=1, column=0, padx=10, pady=10)
        # adeLab = tk.Label(adeLayout, text="Adelaide").grid(row=1, column=1, padx=10, pady=10)
        # hobLab = tk.Label(hobLayout, text="Hobart").grid(row=1, column=2, padx=10, pady=10)
        # melLab = tk.Label(melLayout, text="Melbourne").grid(row=2, column=0, padx=10, pady=10)
        # perLab = tk.Label(perLayout, text="Perth").grid(row=2, column=1, padx=10, pady=10)
        # window.mainloop()




    # def fetchWeather(location):
    #     match location:
    #         case "can":
    #             url = "http://www.bom.gov.au/fwo/IDN60903/IDN60903.94926.json"
    #         case "syd":
    #             url = "http://www.bom.gov.au/fwo/IDN60901/IDN60901.95766.json"
    #         case "dar":
    #             url = "http://www.bom.gov.au/fwo/IDD60901/IDD60901.95122.json"
    #         case "bri":
    #             url = "http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.json"
    #         case "ade":
    #             url = "http://www.bom.gov.au/fwo/IDS60901/IDS60901.94672.json"
    #         case "hob":
    #             url = "http://www.bom.gov.au/fwo/IDT60901/IDT60901.94970.json"
    #         case "mel":
    #             url = "http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json"
    #         case "per":
    #             url = "http://www.bom.gov.au/fwo/IDW60901/IDW60901.94608.json"

    #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'} # needed to authenticate, need user-agnt
    #     request = requests.get(url, headers=headers)
    #     jsonContent = json.loads(request.content)
    #     print(jsonContent['observations']['data'][0]['name']) # this is index for station location
    #     print(jsonContent['observations']['data'][0]["local_date_time"])
    #     print(jsonContent['observations']['data'][0]["air_temp"]) # 0 is the most recent weather report
    #     if (jsonContent['observations']['data'][0]["cloud"] == "-"):
    #         print("Clear")
    #     else:
    #         print(jsonContent['observations']['data'][0]["cloud"])
    #     print(str(jsonContent['observations']['data'][0]["rel_hum"]) + '%')

app = QApplication([])
window = MainWindow()
window.show()

app.exec()
