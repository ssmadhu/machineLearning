from typing import Text
from textblob import TextBlob

# file1 = open('conjuring1.txt', encoding="utf-8")
# file2 = open('myfile.txt', 'w', encoding="utf-8")
# Lines = file1.read()
# print(TextBlob(Lines).sentiment.polarity)
# # for line in Lines:
# #     testimonial = TextBlob(line)
# #     file2.write(line + " Polarity =>" + str(testimonial.sentiment.polarity) + " subjectivity =>" + str(testimonial.sentiment.subjectivity))


import pandas as pd
import numpy as np
col=['date', 'comments']
polarity = []
subjectivity = []
data=pd.read_csv("conjuring_Final1.csv", names=col)
for line in data['comments']:
    testimonial = TextBlob(str(line))
    polarity.append(str(testimonial.sentiment.polarity))
    subjectivity.append(str(testimonial.sentiment.subjectivity))
  #  print("Polarity =>" + str(testimonial.sentiment.polarity) + " subjectivity =>" + str(testimonial.sentiment.subjectivity))
    # print(" Polarity =>" + str(testimonial.sentiment.polarity) + " subjectivity =>" + str(testimonial.sentiment.subjectivity))
data['polarity'] = polarity
data['subjectivity'] = subjectivity
data.to_csv('conjuringResults.csv',index=False)