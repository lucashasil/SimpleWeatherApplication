import tkinter as tk
import json
from tkinter.constants import TOP
import requests
#from requests.api import request

def main():
    window = tk.Tk()
    window.title("The Weather")

    canFrame = tk.Frame(window).grid()
    sydFrame = tk.Frame(window).grid()
    darFrame = tk.Frame(window).grid()
    briFrame = tk.Frame(window).grid()
    adeFrame = tk.Frame(window).grid()
    hobFrame = tk.Frame(window).grid()
    melFrame = tk.Frame(window).grid()
    perFrame = tk.Frame(window).grid()

    canLab = tk.Label(canFrame, text="Canberra").grid(row=0, column=0, padx=10, pady=10)
    sydLab = tk.Label(sydFrame, text="Sydney").grid(row=0, column=1, padx=10, pady=10)
    darLab = tk.Label(darFrame, text="Darwin").grid(row=0, column=2, padx=10, pady=10)
    briLab = tk.Label(briFrame, text="Brisbane").grid(row=1, column=0, padx=10, pady=10)
    adeLab = tk.Label(adeFrame, text="Adelaide").grid(row=1, column=1, padx=10, pady=10)
    hobLab = tk.Label(hobFrame, text="Hobart").grid(row=1, column=2, padx=10, pady=10)
    melLab = tk.Label(melFrame, text="Melbourne").grid(row=2, column=0, padx=10, pady=10)
    perLab = tk.Label(perFrame, text="Perth").grid(row=2, column=1, padx=10, pady=10)
    window.mainloop()


def fetchWeather(location):
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
    print(jsonContent['observations']['data'][0]['name']) # this is index for station location
    print(jsonContent['observations']['data'][0]["local_date_time"])
    print(jsonContent['observations']['data'][0]["air_temp"]) # 0 is the most recent weather report
    if (jsonContent['observations']['data'][0]["cloud"] == "-"):
        print("Clear")
    else:
        print(jsonContent['observations']['data'][0]["cloud"])
    print(str(jsonContent['observations']['data'][0]["rel_hum"]) + '%')

    

main()

