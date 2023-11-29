import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

import random

testDf = pd.DataFrame(columns={
    'date': datetime,
    'tempF': float,
    'tempC' : float,
    'humidity' : float
})

datePoint = datetime.now() - relativedelta(years = 1)

i = 0
for i in range(0, 10000):

    datePoint = datePoint + relativedelta(minutes= 5)
    tempFPoint = random.uniform(45, 80)
    tempCPoint = (tempFPoint - 32) * 5/9
    humidityPoint =random.uniform(55, 97)

    testDf = testDf._append({
        'date': datePoint,
        'tempF': tempFPoint,
        'tempC' : tempCPoint,
        'humidity' : humidityPoint
        },
        ignore_index=True)
    
    i = i+1

testDf.to_csv('./Greenhouse/Setup/testDf.csv', index=False)
