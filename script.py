import matplotlib
import matplotlib.pyplot as plt

# Configure matplotlib to write PNG files
matplotlib.use('Agg')

# Get some x-values
xAxis = list(range(-20,20))

# Write a function to build our y-values
def parabola(xValues):
  # create an empty list to store results
  yValues = []
  # get each number in the given list of x-values
  for x in xValues:
    # compute the square of each value
    y = x*x
    # add the squared value to the list of results
    yValues.append(y)
  # give the resultant list of squared valuse to the caller of this function 
  return yValues

# Get some y-values (by calling our new function)
yAxis = parabola(xAxis)

# We don't have to use all the data we create. We 
# can "slice" out protions that we want.
sliceXAxis  = xAxis[:]
sliceYAxis  = yAxis[:]

# Plot data points as a red circle.
style = 'ro'

# Give matplotlib our data
plt.plot(sliceXAxis , sliceYAxis , style)

# Specify the region of the plot we wish to display
plt.axis([-20, 20, 0, 400])

# Save our plot to the local disk drive
filename = 'graph.png'
plt.savefig(filename)