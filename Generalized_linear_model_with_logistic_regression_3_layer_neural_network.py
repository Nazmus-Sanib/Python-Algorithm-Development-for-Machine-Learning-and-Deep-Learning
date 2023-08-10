# A neural network with only three layer with Generalizaed  Linear Model and Logistic Regression
# Input layer; hidden layer: feature matrix (logistic regression), GLM; output layer: softmax function (calculation of probability)

import numpy as np


x = np.random.randint(0,256, 255)  # Input layer

max_ = np.nanmax(x)
x = x/max_     # Normalized input


M = 3  # Heighest power

# First hidden layer

def feature_matrix(input_layer,M):

  # The feature matrix is defined by the [1 x1 x1^2 xx1^3 x2 x2^2 x2^3 ...... xn xn^2 xn^3]
  # Initialization of the feature matrix

  phi = [1]

  for i in input_layer:

    for j in np.arange(1,M+1,1):
      
      # Updating the feature matrix
      phi.append(i**j)

  return np.array(phi)

def GLM_model(input_layer,M):


  phi = feature_matrix(input_layer,M)

  # Initialize GLM
  glm = phi*np.random.random(len(phi))

  return glm


# Output layer:

# Softmax activation function
def activation_softmax(input_layer,M):

  glm = GLM_model(input_layer,M)

  total_exponential = np.nansum(np.array([2.718281828459045**i for i in glm]))

  softmax = np.array([2.718281828459045**i/total_exponential for i in glm])

  return softmax


activation_softmax(x,M)
