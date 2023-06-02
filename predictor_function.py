# Predictor

# Gaussian For Predictor

def gauss_for_predictor(list_):

  data, weight,train, variance, model_order = list_
  
  
  if not type(weight) == type(np.array([0,1])):
    
    print("Error 1: The data type of the weigth is not numpy ndarray")

    return None
  
  if model_order == False:
    model_order = len(weight)


  # Mean

  mu = weight*(data**np.array([i for i in range(model_order)]))

   

  # Standard deviation of the data
  std = variance**2


  # exponential term of the gaussian distribution

  exp_ = np.exp(-(data-mu)**2/(2*std**2), dtype = np.float128)

  # Denominator of the Gaussian distribution

  denmtr = std*((2*np.pi)**0.5)

  # Gaussian Distribution

  y = (1/denmtr)*exp_

  return y


def array_gauss_for_predictor(datas, weight,train, variance, model_order = False):

  args = [[data,  weight,train, variance, model_order] for data in datas]

  Pr = sum([i for i in map(gauss_for_predictor, args)])

  return Pr


def empirical_loss(datas, weight,train, variance, model_order = False):

  array_probability = array_gauss_for_predictor(datas, weight,train, variance, model_order)

  loss = datas-array_probability

  return loss







