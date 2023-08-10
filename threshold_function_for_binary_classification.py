#Threshold function

import numpy as np

label = np.empty(100)

x = np.random.random(100)

theta  = 0.5


for i in range(len(label)):
  if  x[i] < theta:
    label[i] = 0
  elif x[i] >= theta:
    label[i] = 1


print(x,label)
