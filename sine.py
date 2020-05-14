import math

def sinePlotX(maxXaxis, digits):
    if int(maxXaxis) == maxXaxis or digits < 2:
        return range(0, int(maxXaxis))
    else:
        xAxis = []
        betterXAxis = int(maxXaxis*10**digits)
        for i in range(0, betterXAxis+1):
            xAxis.append(i/10**digits)
        return xAxis

def sinePlotY(xAxis):
    yList = []
    for i in xAxis:
        yList.append(math.sin(i))
    return yList