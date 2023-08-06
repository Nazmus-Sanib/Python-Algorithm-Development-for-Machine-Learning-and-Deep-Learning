# Bernoullis Model
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

N = [77,33]
N_1 = N[1]
N_0 = N[0]

mu = np.linspace(0,1,1000)
Bern_xn_mu = mu**(N_1)*(1-mu)**(N_0)

plt.plot(Bern_xn_mu)

plt.show()



# Beta Distribution

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")

mu = np.linspace(0,1,1000)

aS = np.arange(1,6,1)

bS = aS.copy()

BetaS = []
for i in range(len(aS)):
  for j in range(len(bS)):

    BetaS_ = (mu**(aS[i]-1))*(1-mu)**(bS[j]-1)

    BetaS.append([BetaS_,aS[i], bS[j]])

    plt.plot(mu,BetaS_, label = "aS = {a} bS = {b}".format(a = aS[i], b = bS[i]))

plt.legend(bbox_to_anchor=(0., 0.92, 1.4, .102))
plt.show()




# Beta Bernoulis Model

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")

mu = np.linspace(0,1,1000)

aS = np.arange(1,6,1)

bS = aS.copy()

N_1 = 33

N_0 = 67

BetaS = []
for i in range(len(aS)):
  for j in range(len(bS)):

    BetaS_ = (mu**(N_1+aS[i]-1))*(1-mu)**(N_0+bS[j]-1)

    mu_MAP = np.round((aS[i]+N_1-1)/(aS[i]+bS[i]+N_1+N_0-2),2)

    BetaS.append([BetaS_,aS[i], bS[j], mu_MAP])

    plt.plot(mu,BetaS_, label = "aS = {a} bS = {b} Mean_Parameter_MAP = {um}".format(a = aS[i], b = bS[i], um=  mu_MAP))



plt.legend(bbox_to_anchor=(0., 0.92, 1.8, .102))
plt.show()

