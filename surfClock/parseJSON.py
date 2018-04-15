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
        # apiRequest = requests.get('http://magicseaweed.com/api/19443130b5ae2758d1b254b8da7ea460/forecast/?spot_id=279&fields=localTimestamp,fadedRating,solidRating,swell.*,wind.speed,wind.unit,wind.compassDirection')
        # apiResponse = apiRequest.json()
        apiResponse = [{
        "localTimestamp": 1523750400,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 1.14,
            "absMaxBreakingHeight": 1.77,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 1.1,
                    "period": 15,
                    "direction": 22.97,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 0.9,
                    "period": 15,
                    "direction": 23.47,
                    "compassDirection": "SSW"
                },
                "secondary": {
                    "height": 0.4,
                    "period": 3,
                    "direction": 63.25,
                    "compassDirection": "WSW"
                }
            }
        },
        "wind": {
            "speed": 1,
            "compassDirection": "W",
            "unit": "mph"
        }},{
        "localTimestamp": 1523761200,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 1.15,
            "absMaxBreakingHeight": 1.8,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 1.1,
                    "period": 15,
                    "direction": 20.95,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 0.9,
                    "period": 15,
                    "direction": 22.78,
                    "compassDirection": "SSW"
                },
                "secondary": {
                    "height": 0.5,
                    "period": 3,
                    "direction": 63.22,
                    "compassDirection": "WSW"
                }
            }
        },
        "wind": {
            "speed": 2,
            "compassDirection": "ESE",
            "unit": "mph"
        }},{
        "localTimestamp": 1523772000,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 1.01,
            "absMaxBreakingHeight": 1.57,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 1.2,
                    "period": 15,
                    "direction": 20.61,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 0.8,
                    "period": 15,
                    "direction": 16.15,
                    "compassDirection": "SSW"
                },
                "secondary": {
                    "height": 0.6,
                    "period": 4,
                    "direction": 65.51,
                    "compassDirection": "WSW"
                }
            }
        },
        "wind": {
            "speed": 2,
            "compassDirection": "SE",
            "unit": "mph"
        }},{
        "localTimestamp": 1523782800,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 0.9,
            "absMaxBreakingHeight": 1.41,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 1,
            "components": {
                "combined": {
                    "height": 1.3,
                    "period": 15,
                    "direction": 21,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 0.7,
                    "period": 15,
                    "direction": 13.3,
                    "compassDirection": "SSW"
                },
                "secondary": {
                    "height": 0.7,
                    "period": 4,
                    "direction": 68.11,
                    "compassDirection": "WSW"
                }
            }
        },
        "wind": {
            "speed": 5,
            "compassDirection": "SSE",
            "unit": "mph"
        }},{
        "localTimestamp": 1523793600,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 0.97,
            "absMaxBreakingHeight": 1.51,
            "probability": 95,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 1.3,
                    "period": 14,
                    "direction": 21.56,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 0.8,
                    "period": 14,
                    "direction": 14.15,
                    "compassDirection": "SSW"
                },
                "secondary": {
                    "height": 0.8,
                    "period": 4,
                    "direction": 69.83,
                    "compassDirection": "WSW"
                }
            }
        },
        "wind": {
            "speed": 7,
            "compassDirection": "SSW",
            "unit": "mph"
        }},{
        "localTimestamp": 1523804400,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 1,
            "absMaxBreakingHeight": 1.56,
            "probability": 95,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 1.3,
                    "period": 14,
                    "direction": 22.56,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 0.8,
                    "period": 14,
                    "direction": 17.3,
                    "compassDirection": "SSW"
                },
                "secondary": {
                    "height": 0.4,
                    "period": 14,
                    "direction": 43.11,
                    "compassDirection": "SW"
                },
                "tertiary": {
                    "height": 0.8,
                    "period": 4,
                    "direction": 69.88,
                    "compassDirection": "WSW"
                }
            }
        },
        "wind": {
            "speed": 6,
            "compassDirection": "SW",
            "unit": "mph"
        }},{
        "localTimestamp": 1523815200,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 0.94,
            "absMaxBreakingHeight": 1.48,
            "probability": 95,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 1,
            "components": {
                "combined": {
                    "height": 1.4,
                    "period": 14,
                    "direction": 23.49,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 0.8,
                    "period": 14,
                    "direction": 13.1,
                    "compassDirection": "SSW"
                },
                "secondary": {
                    "height": 0.5,
                    "period": 15,
                    "direction": 48.5,
                    "compassDirection": "SW"
                },
                "tertiary": {
                    "height": 0.9,
                    "period": 4,
                    "direction": 68.98,
                    "compassDirection": "WSW"
                }
            }
        },
        "wind": {
            "speed": 5,
            "compassDirection": "WSW",
            "unit": "mph"
        }},{
        "localTimestamp": 1523826000,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 1.01,
            "absMaxBreakingHeight": 1.58,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 1.9,
                    "period": 14,
                    "direction": 18.06,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 0.8,
                    "period": 14,
                    "direction": 17.47,
                    "compassDirection": "SSW"
                },
                "secondary": {
                    "height": 1.5,
                    "period": 5,
                    "direction": 67.84,
                    "compassDirection": "WSW"
                }
            }
        },
        "wind": {
            "speed": 4,
            "compassDirection": "W",
            "unit": "mph"
        }},{
        "localTimestamp": 1523836800,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 1.16,
            "absMaxBreakingHeight": 1.81,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 2,
                    "period": 14,
                    "direction": 19.06,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 1.8,
                    "period": 5,
                    "direction": 69.42,
                    "compassDirection": "WSW"
                },
                "secondary": {
                    "height": 0.7,
                    "period": 14,
                    "direction": 11.08,
                    "compassDirection": "S"
                }
            }
        },
        "wind": {
            "speed": 5,
            "compassDirection": "W",
            "unit": "mph"
        }},{
        "localTimestamp": 1523847600,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 1.17,
            "absMaxBreakingHeight": 1.83,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 2,
                    "period": 14,
                    "direction": 20.61,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 1.8,
                    "period": 5,
                    "direction": 69.73,
                    "compassDirection": "WSW"
                },
                "secondary": {
                    "height": 0.7,
                    "period": 14,
                    "direction": 10.84,
                    "compassDirection": "S"
                }
            }
        },
        "wind": {
            "speed": 7,
            "compassDirection": "W",
            "unit": "mph"
        }},{
        "localTimestamp": 1523858400,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 1.2,
            "absMaxBreakingHeight": 1.88,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 1,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 2,
                    "period": 14,
                    "direction": 22.71,
                    "compassDirection": "SSW"
                },
                "primary": {
                    "height": 1.9,
                    "period": 5,
                    "direction": 71.34,
                    "compassDirection": "WSW"
                },
                "secondary": {
                    "height": 0.7,
                    "period": 13,
                    "direction": 10.82,
                    "compassDirection": "S"
                },
                "tertiary": {
                    "height": 0.4,
                    "period": 16,
                    "direction": 77.12,
                    "compassDirection": "WSW"
                }
            }
        },
        "wind": {
            "speed": 9,
            "compassDirection": "W",
            "unit": "mph"
        }},{
        "localTimestamp": 1523869200,
        "fadedRating": 0,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 1.59,
            "absMaxBreakingHeight": 2.48,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 2,
            "maxBreakingHeight": 2,
            "components": {
                "combined": {
                    "height": 3,
                    "period": 5,
                    "direction": 70.16,
                    "compassDirection": "WSW"
                },
                "primary": {
                    "height": 2.5,
                    "period": 5,
                    "direction": 72.49,
                    "compassDirection": "WSW"
                },
                "secondary": {
                    "height": 0.7,
                    "period": 13,
                    "direction": 11.27,
                    "compassDirection": "SSW"
                },
                "tertiary": {
                    "height": 0.4,
                    "period": 14,
                    "direction": 46.22,
                    "compassDirection": "SW"
                }
            }
        },
        "wind": {
            "speed": 13,
            "compassDirection": "W",
            "unit": "mph"
        }},{
        "localTimestamp": 1523880000,
        "fadedRating": 1,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 2.17,
            "absMaxBreakingHeight": 3.39,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 2,
            "maxBreakingHeight": 3,
            "components": {
                "combined": {
                    "height": 4,
                    "period": 6,
                    "direction": 74.4,
                    "compassDirection": "WSW"
                },
                "primary": {
                    "height": 4,
                    "period": 6,
                    "direction": 74.81,
                    "compassDirection": "WSW"
                },
                "secondary": {
                    "height": 0.7,
                    "period": 13,
                    "direction": 11.87,
                    "compassDirection": "SSW"
                },
                "tertiary": {
                    "height": 0.5,
                    "period": 14,
                    "direction": 46.5,
                    "compassDirection": "SW"
                }
            }
        },
        "wind": {
            "speed": 20,
            "compassDirection": "W",
            "unit": "mph"
        }},{
        "localTimestamp": 1523890800,
        "fadedRating": 1,
        "solidRating": 0,
        "swell": {
            "absMinBreakingHeight": 2.56,
            "absMaxBreakingHeight": 4,
            "probability": 100,
            "unit": "ft",
            "minBreakingHeight": 3,
            "maxBreakingHeight": 4,
            "components": {
                "combined": {
                    "height": 5,
                    "period": 6,
                    "direction": 76.46,
                    "compassDirection": "WSW"
                },
                "primary": {
                    "height": 5,
                    "period": 6,
                    "direction": 76.24,
                    "compassDirection": "WSW"
                },
                "secondary": {
                    "height": 0.7,
                    "period": 13,
                    "direction": 9.26,
                    "compassDirection": "S"
                },
                "tertiary": {
                    "height": 0.6,
                    "period": 15,
                    "direction": 39.36,
                    "compassDirection": "SW"
                }
            }
        },
        "wind": {
            "speed": 25,
            "compassDirection": "W",
            "unit": "mph"
        }}]
        # print 'pretty api response: ', json.dumps(apiResponse, sort_keys = True, indent = 4)

        return apiResponse

    except:
        print "ERROR: Server did not return a response"


def parseSurfData(surfCast):
    i = 0
    currentTime = int(time.time())
    print "Current Time: ", time.ctime(currentTime)

    try:
        while i < 40:
            # gets the most recent forecast that's less than 3 hours old
            if (10800 > (currentTime - surfCast[i]['localTimestamp'])) and ((currentTime - surfCast[i]['localTimestamp']) > 0):
                # print "current forecast: ", surfCast[i]['localTimestamp']

                # this is the number of the item in the JSON object corresponding to the current forecast
                currentForecast = i
                print "Current Forecast Number: ", currentForecast

                break

            # increment to the next forecast in the JSON object
            else:
                i += 1

# parse the JSON response object using the current forecast number from above
        print "Last forecast was:", time.ctime(surfCast[currentForecast]['localTimestamp'])
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

# print forecast components in readable form
        print
        print breakName
        print 'Local Time: ', localTimestamp
        print 'Solid Star Rating:', str(solidRating) + ' star(s)'
        print 'Faded Star Rating:', str(fadedRating) + ' star(s)'
        print 'Combined Star Rating:', str(combinedStarRating) + ' star(s)'
        print 'Combined Swell Height:', str(combinedSwellHeight) + 'ft'
        print 'Min Breaking Height:', str(minBreakingHeight) + 'ft'
        print 'Max Breaking Height:', str(maxBreakingHeight) + 'ft'
        print 'WindSpeed:', str(windSpeed) + 'mph'
        print 'Compass Direction:', str(compassDirection)
        print

    except:
        print "ERROR: Couldn't format data"

# runs all functions in one go
def main():
    try:
        surfData = updateSurfData()
        parseSurfData(surfData)
    except:
        print "ERROR: Main function couldn't complete"

main()
