import sine
import matplotlib
import matplotlib.pyplot as plt
import math


#Change this code:

#The maximum X-value on your chart
maxRange = 6.28
#The number of digits on the graph
digits = 2
#To learn how to change the style of the graph, go to https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
style = 'g-'


#Leave this code alone:
xAxis = sine.sinePlotX(maxRange, digits)
yAxis = sine.sinePlotY(xAxis)

plt.plot(xAxis , yAxis , style)
plt.axis([0, maxRange + 0.1, -1, 1])
filename = 'graph.png'
plt.savefig(filename)