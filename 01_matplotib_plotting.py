#1

import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()

# Plotting with line

import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints)
plt.show()

# Plotting without line

import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints, 'o')
plt.show()

#4

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

#5

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 1])
plt.title('My First Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

#6

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
plt.plot(x, y)
plt.title("Simple Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

#7

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [30, 20, 15, 10]
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2', linestyle='--')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Lines')
plt.legend()
plt.show()

# Sine and Cosine Curves

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='Sine Wave')
plt.plot(x, y2, label='Cosine Wave', linestyle='--')
plt.title('Sine and Cosine Curves')
plt.legend()
plt.show()

# Exponential Growth

import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [2, 4, 8, 16, 32]
plt.plot(x, y, marker='o')
plt.title('Exponential Growth')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# Multiple Points

import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()

# Default X-Points

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()