# @authors: Cooper Pearson, Daniel Hoy
# @version: 1.0
#RPi.GPIO as gpio
import threading, time, json, requests


def updateSurfData():
    # set up a secondary thread so that the clock can run concurrently with the update data function
    # threading.Timer(7200.0, updateSurfData).start()

    # run API call that returns the forecast data in JSON format
    try:
        apiRequest = requests.get('http://magicseaweed.com/api/19443130b5ae2758d1b254b8da7ea460/forecast/?spot_id=279&fields=localTimestamp,fadedRating,solidRating,swell.*,wind.speed,wind.unit,wind.compassDirection')
        apiResponse = apiRequest.json()
        print 'apiResponse', apiResponse #doesn't work

        return apiResponse

    except:
        print("ERROR: Server did not return a response")


def parseSurfData(surfData):
    # parse the JSON response and set variables based on keys in response
    try:
        localTimestamp = time.strftime('%H:%M:%S %m-%d-%Y', time.localtime(surfData['localTimestamp']))
        # solidRating = apiResponse['solidRating']
        # fadedRating = apiResponse['fadedRating']
        # combinedStarRating = apiResponse['solidRating'] - apiResponse['fadedRating']
        # combinedSwellHeight = apiResponse['swell']['components']['combined']['height']
        # minBreakingHeight = apiResponse['swell']['maxBreakingHeight']
        # maxBreakingHeight = apiResponse['swell']['minBreakingHeight']
        # windSpeed = apiResponse['wind']['speed']
        # compassDirection = apiResponse['wind']['compassDirection']
        # breakName = "Malibu First Point"

        print 'full api response: ', json.dumps(surfData)
        # print 'full api response: ', json.dumps(apiResponse, sort_keys = True, indent = 4)
        print
        print breakName
        print 'localTimestamp: ', localTimestamp
        print 'solidRating:', str(solidRating) + ' star(s)'
        print 'fadedRating:', str(fadedRating) + ' star(s)'
        print 'combinedStarRating:', str(combinedStarRating) + ' star(s)'
        print 'combined swell height:', str(combinedSwellHeight) + 'ft'
        print 'min breaking height:', str(minBreakingHeight) + 'ft'
        print 'max breaking height:', str(maxBreakingHeight) + 'ft'
        print 'windSpeed:', str(windSpeed) + 'mph'
        print 'compass direction:', str(compassDirection)

    except:
        print("ERROR: Couldn't format data received")

    # # set gpio pin brightnesses
    # try:
    #
    #
    # except:
    #     print("ERROR: Couldn't set GPIO pins, is the Raspberry Pi properly connected?")

def setGPIOPins():
    try:
        print(gpio.RPI_INFO)

    except:
        print("ERROR: Couldn't find GPIO pins")


updateSurfData()
parseSurfData(apiResponse)
