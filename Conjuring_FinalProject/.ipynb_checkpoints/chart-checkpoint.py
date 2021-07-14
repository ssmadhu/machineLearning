
import pandas as pd
import numpy as np
col=['date','polarity','subjectivity','comments']
polarity = []
subjectivity = []
data=pd.read_csv("conjuringResults.csv", names=col)
print(data.groupby(['date']).size)