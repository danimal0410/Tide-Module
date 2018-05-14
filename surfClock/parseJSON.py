# @authors: Cooper Pearson, Daniel Hoy
# @version: 1.0
#RPi.GPIO as gpio
from datetime import datetime
import threading, time, json, requests


def updateSurfData():
# set up a secondary thread so that the clock can run concurrently with the update data function
# threading.Timer(7200.0, updateSurfData).start()

# get request to send to MSW API that returns the forecast data in JSON format
    try:
        apiRequest = requests.get('http://magicseaweed.com/api/19443130b5ae2758d1b254b8da7ea460/forecast/?spot_id=279&fields=localTimestamp,fadedRating,solidRating,swell.*,wind.speed,wind.unit,wind.compassDirection')
        apiResponse = apiRequest.json()
        # print ('pretty api response: ', json.dumps(apiResponse, sort_keys = True, indent = 4))

        return apiResponse

    except:
        print("ERROR: Server did not return a response")


def parseSurfData(surfCast):
    i = 0
    currentTime = int(time.time())
    print("Current Time: ", time.ctime(currentTime))

    try:
        while i < 40:
            # gets the most recent forecast that's less than 3 hours old
            if (10800 > (currentTime - surfCast[i]['localTimestamp'])) and ((currentTime - surfCast[i]['localTimestamp']) > 0):
                # print("current forecast: ", surfCast[i]['localTimestamp'])

                # this is the number of the item in the JSON object corresponding to the current forecast
                currentForecast = i
                print("Current Forecast Number: ", currentForecast)

                break

            # increment to the next forecast in the JSON object
            else:
                i += 1

# parse the JSON response object using the current forecast number from above
        print("Last forecast was:", time.ctime(surfCast[currentForecast]['localTimestamp']))
        localTimestamp = time.strftime('%H:%M:%S %m-%d-%Y', time.localtime(surfCast[currentForecast]['localTimestamp']))
        solidRating = surfCast[currentForecast]['solidRating']
        fadedRating = surfCast[currentForecast]['fadedRating']
        combinedStarRating = surfCast[currentForecast]['solidRating'] - surfCast[currentForecast]['fadedRating']
        combinedSwellHeight = surfCast[currentForecast]['swell']['components']['combined']['height']
        minBreakingHeight = surfCast[currentForecast]['swell']['maxBreakingHeight']
        maxBreakingHeight = surfCast[currentForecast]['swell']['minBreakingHeight']
        windSpeed = surfCast[currentForecast]['wind']['speed']
        compassDirection = surfCast[currentForecast]['wind']['compassDirection']
        breakName = "Malibu First Point"

# output forecast components to console in readable form
        print()
        print(breakName)
        print('Local Time: ', localTimestamp)
        print('Solid Star Rating:', str(solidRating) + ' star(s)')
        print('Faded Star Rating:', str(fadedRating) + ' star(s)')
        print('Combined Star Rating:', str(combinedStarRating) + ' star(s)')
        print('Combined Swell Height:', str(combinedSwellHeight) + 'ft')
        print('Min Breaking Height:', str(minBreakingHeight) + 'ft')
        print('Max Breaking Height:', str(maxBreakingHeight) + 'ft')
        print('WindSpeed:', str(windSpeed) + 'mph')
        print('Compass Direction:', str(compassDirection))
        print()

    except:
        print("ERROR: Couldn't format data")

# setting up LED output through GPIO pins based on forecast components
def updateLEDS():
    try:
        print("length of combined star rating", len(combinedStarRating))

        if (len(combinedStarRating) == 0):
            print("Star Rating is 0, go back to sleep brah")
            # "0": reset all LED pins

        elif (len(combinedStarRating) == 1):
            # "1":0x80
            print("Star Rating might as well be 0, go back to sleep Chad")

        elif (len(combinedStarRating) == 2):
            # "2":0xC0
            print("Star Rating is 2, are you craving it?")

        elif (len(combinedStarRating) == 3):
            # "3":0xE0
            print("Star Rating is 3, yup totally worth it c'mon bud")

        elif (len(combinedStarRating) == 4):
            # "4":0xF0
            print("Star Rating is 4, time to get gnarly")

        elif (len(combinedStarRating) == 5):
            # "5":0xF8
            print("Star Rating is 3, GET PITTED SO PITTED")

    except:
        print("ERROR: Couldn't update LEDs with new data")

# runs all functions in one go
def main():
    try:
        surfData = updateSurfData()
        parseSurfData(surfData)
        # updateLEDS()
    except:
        print("ERROR: Main function couldn't complete")

main()
