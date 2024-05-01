def maxPool2D(output_convolution2d,shape):

  if not type(shape) == type([2,2]) or type(shape) == type((2,2)):
    return """Shape must be a tuple or list object. 
              For example, shape = [2,2] or shape = (2,2)."""
  elif not len(shape) == 2:
    return "Window of the 2d maxpool matrix have to be two dimensional."
  elif not shape[0] == shape[1]:
    return "Window of the maxpool matrix must be a square matrix."

  matrix = output_convolution2d.copy()

  maxpool = np.zeros([int((matrix.shape[0]-
         shape[0]) +1),int((matrix.shape[1]
         - shape[1])+1)])

  for i in range(maxpool.shape[0]-shape[0]):
    for j in range(maxpool.shape[1]-shape[1]):
      maxpool[i,j] = np.nanmax(np.array([np.array(
                  [matrix[i+z][j+i2]
                  for i2 in range(shape[1])])
                  for z in range(shape[0])]))
      
  return maxpool

