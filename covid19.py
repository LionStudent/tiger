import requests


import matplotlib

import matplotlib.pyplot as plt

matplotlib.use('Agg')


import process


def getImageFilename(options):

    startDate = options["from"]

    endDate = options["to"]

    days = getDailyMeasurements(startDate, endDate)


    measurementName = options["metric"]

    measurements = process.extract(days, measurementName)


    if not options["isTotal"]:

        measurements= process.dailyIncrease(measurements)


    if not options["isRaw"]:

        measurements= process.sevenDayAverage(measurements)


    numMeasurements = len(measurements)

    dayCounter = range(1, numMeasurements+1)

    filename = saveImage(dayCounter, measurements)

    return filename


def getDailyMeasurements(startDate, endDate):

    endpoint = 'https://api.covid19api.com/'

    resource = 'total/country/united-states'

    parameters = '?from=%s&to=%s' % (startDate, endDate)


    response = requests.get(endpoint+resource+parameters)

    return response.json()


def saveImage(xValues, yValues):

    dpi = 72

    width = 640

    height = 480

    plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)


    style = 'ro'

    xMax = xValues[len(xValues)-1]

    yMax = max(yValues)

    plt.plot(xValues, yValues, style)

    plt.axis([0, xMax, 0, yMax])


    filename = 'graph.png'

    plt.savefig(filename)

    plt.clf()

    return filename

