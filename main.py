import tkinter as tk
import json
import requests
#from requests.api import request

# def main():

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
    print(jsonContent['observations']['header'][0]['name']) # this is index for station location

    

fetchWeather("per")