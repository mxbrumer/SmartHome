import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

testDf = pd.read_csv('./Greenhouse/Setup/testDf.csv')

#######################################################################################

###################     Histigram for Each Distribution     ###########################

#######################################################################################

# F Temp
plt.hist(testDf['tempF'])
plt.title('Distribution of Synthetic F Temp')
plt.show()

# C Temp
plt.hist(testDf['tempC'])
plt.title('Distribution of Synthetic C Temp')
plt.show()

# Humidity
plt.hist(testDf['humidity'])
plt.title('Distribution of Synthetic Humidity')
plt.show()



#######################################################################################

###################     Temp and Humidity Across Time     #############################

#######################################################################################

# Temp Accross Time
plt.plot(testDf['date'][0:75], testDf['tempF'][0:75])
plt.xticks([])
plt.title('Temp and Time')
plt.ylabel('Temp (F)')
plt.xlabel('Time')
plt.show()
