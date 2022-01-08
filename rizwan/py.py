import matplotlib.pyplot as plt
import matplotlib.colors
 
# Prepare a list of integers
val = [2, 3, 6, 9, 14]
 
# Prepare a list of sizes that increases with values in val
sizevalues = [i**2*50+50 for i in val]
 
# Prepare a list of colors
plotcolor = ['red','orange','yellow','green','blue']
 
# Draw a scatter plot of val points with sizes in sizevalues and
# colors in plotcolor
plt.scatter(val, val, s=sizevalues, c=plotcolor)
 
# Draw grid lines with red color and dashed style
plt.grid(color='red', linestyle='-.', linewidth=0.7)
 
# Set axis limits to show the markers completely
plt.xlim(0, 20)
plt.ylim(0, 20)
 
plt.show()
