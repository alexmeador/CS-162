#CS 162 Graphic File Exercise
#Alex Meador

import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['red', 'green', 'pink', 'yellow' ]
explodelist = [0.05, 0.05, 0.05, 0.05]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    explode = explodelist, startangle = 180)
plot.axis('equal')
plot.savefig('piechart.png')
