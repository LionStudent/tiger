import sine
import matplotlib
import matplotlib.pyplot as plt
import math

maxRange = 6.28

xAxis = sine.sinePlotX(maxRange, 2)
yAxis = sine.sinePlotY(xAxis)

style = 'ro'
plt.plot(xAxis , yAxis , style)
plt.axis([0, maxRange + 0.1, -1, 1])
filename = 'graph.png'
plt.savefig(filename)