import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [1,3,9,27]
plt.plot(x,y, 'co')
# specify xmin, xmax, ymin, ymax of axis
plt.axis([0,6,0,30])

# uniformly sample points at .2 intervals
t = np.arange(0, 5, 0.2)
plt.plot(t,t)
plt.show()