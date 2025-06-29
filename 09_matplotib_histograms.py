# Create Histogram

import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()

# Students' Exam Scores

import matplotlib.pyplot as plt
import numpy as np
scores = np.random.normal(75, 12, 300)
plt.hist(scores, bins=10, color='skyblue', edgecolor='black')
plt.title("Exam Scores Distribution")
plt.xlabel("Scores")
plt.ylabel("Number of Students")
plt.show()

# People's Heights

import matplotlib.pyplot as plt
import numpy as np
heights = np.random.normal(165, 15, 200)
plt.hist(heights, bins=8, color='green', edgecolor='black')
plt.title("Height Distribution")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()

# Daily Temperatures (°C)

import matplotlib.pyplot as plt
import numpy as np
temperatures = np.random.normal(30, 5, 150)
plt.hist(temperatures, bins=12, color='orange', edgecolor='black')
plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Days")
plt.show()

# Salaries of Employees (in thousands)

import matplotlib.pyplot as plt
import numpy as np
salaries = np.random.normal(60, 20, 250)
plt.hist(salaries, bins=10, color='purple', edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary (in 1000s)")
plt.ylabel("Number of Employees")
plt.show()
