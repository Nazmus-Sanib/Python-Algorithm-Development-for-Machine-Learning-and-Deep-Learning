# Testing the script of gaussian distribution


import matplotlib.pyplot as plt
from gaussian_distribution import gaussian_probability as gp

plt.style.use("ggplot")
# Define the data
data = np.exp(np.random.random(1000))

# Plot the Gaussian probability distribution, call the gaussian distribution in here
plt.plot(gp(data))

# Title, xlabel and ylabel
print("Please insert the name of the data or data variable for which the Gaussian distribution have to be determined.\nPress Enter to skip")


title_input = input()

if not title_input:
  title_input = "Data"

plt.title("The Gaussian Distribution of the {}".format(title_input))

plt.xlabel("{}".format(title_input), weight = "bold")

plt.ylabel("Probability", weight = "bold")


plt.show()
