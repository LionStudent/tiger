def extract(days, measurementName):

    measurements = []

    for day in days:

        measurement = day[measurementName]

        measurements.append(measurement)

    return measurements


def sevenDayAverage(measurements):

    averageMeasurements = []

    numMeasurements = len(measurements)

    for i in range(numMeasurements):

        if i < 7:

            continue

        else:

            weekTotal = measurements[i]+measurements[i-1]+measurements[i-2]+measurements[i-3]+measurements[i-4]+measurements[i-5]+measurements[i-6]

            average = weekTotal / 7

            averageMeasurements.append(average)

    return averageMeasurements


def dailyIncrease(measurements):

    differenceMeasurements = []

    numMeasurements = len(measurements)

    for i in range(numMeasurements):

        if i < 1:

            continue

        else:

            difference = measurements[i]-measurements[i-1]

            differenceMeasurements.append(difference)

    return differenceMeasurements

