import matplotlib.pyplot as pyplot
import numpy as np

msg = "hello,我的python程序第一个消息"
print(msg)

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
pyplot.plot(x, np.sin(x))    # Plot the sine of each x point
pyplot.show()                # Display the plot