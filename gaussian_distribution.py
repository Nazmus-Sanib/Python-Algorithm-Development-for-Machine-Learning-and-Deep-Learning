# Calculating Gaussian Distribution
import numpy as np

def gaussian_probability(data):

  # Parameters:
  # data: 1 dimensional

 
  # Casting the data into ndarray if data type as ndarray is false
  if not type(data) == type(np.array([0,1])):
    data = np.array(data)


  # Sort the data: smaller to greater
  data.sort()


  # Mean of the data
  mu = np.nanmean(data, dtype = np.float128)

  # Standard deviation of the data
  std = np.nanstd(data, dtype = np.float128)


  # exponential term of the gaussian distribution

  exp_ = -(data-mu)**2/(2*std**2)

  # Denominator of the Gaussian distribution

  denmtr = std*((2*np.pi)**0.5)

  # Gaussian Distribution

  y = (1/denmtr)*exp_

  return y

  

  
