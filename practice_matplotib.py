# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

# Plotting with line

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

# Plotting without line

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints, 'o')
# plt.show()


# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3], [4, 5, 6])
# plt.show()

# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3], [4, 5, 1])
# plt.title('My First Plot')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.show()


# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [2, 4, 6, 8]

# plt.plot(x, y)
# plt.title("Simple Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y1 = [10, 20, 25, 30]
# y2 = [30, 20, 15, 10]

# plt.plot(x, y1, label='Line 1')
# plt.plot(x, y2, label='Line 2', linestyle='--')

# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.title('Multiple Lines')
# plt.legend()
# plt.show()



# Sine and Cosine Curves

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 2 * np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, label='Sine Wave')
# plt.plot(x, y2, label='Cosine Wave', linestyle='--')
# plt.title('Sine and Cosine Curves')
# plt.legend()
# plt.show()


# Exponential Growth

# import matplotlib.pyplot as plt
# import numpy as np

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 8, 16, 32]

# plt.plot(x, y, marker='o')
# plt.title('Exponential Growth')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid(True)
# plt.show()


# Multiple Points

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

# Default X-Points

# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(ypoints, 'o')
# plt.show()



















# # With round circle

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o')
# plt.show()

# # With *

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = '*')
# plt.show()

# # With H-Line

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = '_')
# plt.show()

# # And a lot of markers can be used as +, 1, 2, <, > etc

# # Marker with Line and Color

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'o:r')
# plt.show()

# # Marker can be used for the line reference too

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'o:')
# plt.show()

# # As '-.'

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'o-.')
# plt.show()

# # Markers can be used for the color reference too

# # For Blue

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'ob')
# plt.show()

# # For white

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'ow')
# plt.show()

# # We can also maintain the size of markers using ms

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()

# # We can also give the color to the markeredge using mec

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()

# # We can also give the color to the inside of marker edges using mfc

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()

# # Both mec and mfc can be used together to give the colors we want

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
# plt.show()








# # LineStyle

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = 'dotted')
# plt.show()

# # Dashed Line

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = 'dashed')
# plt.show()

# # We can also use the shorter syntax of linestyle as 'ls'

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, ls = ':')
# plt.show()

# # None Linestyle

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, ls = '')
# plt.show()

# # We can aslo set the color of line

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, color = 'r')
# plt.show()

# # Plotting with a beautiful green line

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, c = '#4CAF50')
# plt.show()

# # We can use the keyword argument linewidth or the shorter lw to change the width of the line

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linewidth = '20.5')
# plt.show()

# # Multiple Lines

# import matplotlib.pyplot as plt
# import numpy as np
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()

# # More Multiple

# import matplotlib.pyplot as plt
# import numpy as np
# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(x1, y1, x2, y2)
# plt.show()












# # xlabel() and ylabel() functions to set a label for the x- and y-axis.

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x, y)
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.show()

# # Create a Title for a Plot

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x, y)
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.show()

# # We can use fontdict parameter in xlabel(),ylabel(),and title() to set font properties for title and labels.

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
# plt.title("Sports Watch Data", fontdict = font1)
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)
# plt.plot(x, y)
# plt.show()

# # We can use the loc parameter in title() to position the title

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data", loc = 'left')
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
# plt.show()













# # Use grid() function to add grid lines

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
# plt.grid()
# plt.show()

# # We can use the axis parameter in the grid() function to specify which grid lines to display

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
# plt.grid(axis = 'x')
# plt.show()

# # asix='y' along y-axis

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
# plt.grid(axis = 'y')
# plt.show()

# # We can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plt.show()









# # With the subplot() function we can draw multiple plots in one figure

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.show()

# # 2 plots on top of each other

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 1, 1)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 1, 2)
# plt.plot(x,y)
# plt.show()

# # 6 plots

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 2)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 3)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 4)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 5)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 6)
# plt.plot(x,y)
# plt.show()

# # We can add a title to each plot with the title() function

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")
# plt.show()

# # We can add a title to the entire figure with the suptitle() function

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")
# plt.suptitle("MY SHOP")
# plt.show()













# # We can use the scatter() function to draw a scatter plot

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)
# plt.show()

# # Compare plots

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)
# plt.show()

# # We can set your own color for each scatter plot with the color or the c argument

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y, color = 'hotpink')
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y, color = '#88c999')
# plt.show()

# # We can even set a specific color for each dot by using an array of colors as value for the c argument

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# plt.scatter(x, y, c=colors)
# plt.show()

# """
# ColorMap
# The Matplotlib module has a number of available colormaps.
# A colormap is like a list of colors, where each color has a value that ranges from 0 to 100
# """

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# plt.scatter(x, y, c=colors, cmap='viridis')
# plt.colorbar()
# plt.show()

# # There are a lot of built-in colormaps, one of them is following:

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# plt.scatter(x, y, c=colors, cmap='winter_r')
# plt.colorbar()
# plt.show()

# # We can change the size of the dots with the s argument

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# plt.scatter(x, y, s=sizes)
# plt.show()

# # We can adjust the transparency of the dots with the alpha argument

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# plt.scatter(x, y, s=sizes, alpha=0.5)
# plt.show()

# # Combine Color Size and Alpha

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
# plt.colorbar()
# plt.show()











# # Creating Bars

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x,y)
# plt.show()

# # Fruits

# import matplotlib.pyplot as plt
# import numpy as np
# x = ["APPLES", "BANANAS"]
# y = [400, 350]
# plt.bar(x, y)
# plt.show()

# # Horizontal Bars

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.barh(x, y)
# plt.show()

# # Bar Color

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "red")
# plt.show()

# # Color Names

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "hotpink")
# plt.show()

# # Color Hex

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "#4CAF50")
# plt.show()

# # Bar Width

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, width = 0.1)
# plt.show()

# # Note: For horizontal bars, use height instead of width.

# # Bar Height

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.barh(x, y, height = 0.1)
# plt.show()









# # Create Histogram

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.normal(170, 10, 250)
# plt.hist(x)
# plt.show()

# # Students' Exam Scores

# import matplotlib.pyplot as plt
# import numpy as np
# scores = np.random.normal(75, 12, 300)
# plt.hist(scores, bins=10, color='skyblue', edgecolor='black')
# plt.title("Exam Scores Distribution")
# plt.xlabel("Scores")
# plt.ylabel("Number of Students")
# plt.show()

# # People's Heights

# import matplotlib.pyplot as plt
# import numpy as np
# heights = np.random.normal(165, 15, 200)
# plt.hist(heights, bins=8, color='green', edgecolor='black')
# plt.title("Height Distribution")
# plt.xlabel("Height (cm)")
# plt.ylabel("Frequency")
# plt.show()

# # Daily Temperatures (°C)

# import matplotlib.pyplot as plt
# import numpy as np
# temperatures = np.random.normal(30, 5, 150)
# plt.hist(temperatures, bins=12, color='orange', edgecolor='black')
# plt.title("Temperature Distribution")
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Days")
# plt.show()

# # Salaries of Employees (in thousands)

# import matplotlib.pyplot as plt
# import numpy as np
# salaries = np.random.normal(60, 20, 250)
# plt.hist(salaries, bins=10, color='purple', edgecolor='black')
# plt.title("Salary Distribution")
# plt.xlabel("Salary (in 1000s)")
# plt.ylabel("Number of Employees")
# plt.show()














# # Creating Pie Charts

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# plt.pie(y)
# plt.show()

# # Labels

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels)
# plt.show() 

# # Start Angle

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels, startangle = 90)
# plt.show() 

# # Explode(Wedges)

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y, labels = mylabels, explode = myexplode)
# plt.show()

# # Shadow

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
# plt.show() 

# # Colors

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# mycolors = ["black", "hotpink", "b", "#4CAF50"]
# plt.pie(y, labels = mylabels, colors = mycolors)
# plt.show() 

# # Legend

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels)
# plt.legend()
# plt.show() 

# # Legend With Header

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels)
# plt.legend(title = "Four Fruits:")
# plt.show() 

