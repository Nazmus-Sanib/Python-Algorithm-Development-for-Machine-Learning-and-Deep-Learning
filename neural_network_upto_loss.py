def initialize_cnn_weight(kernel_shape,degree_weight_cnn=1):

  return np.random.random(kernel_shape)**degree_weight_cnn


def initialize_dense_weight(dense_layer_shape, degree_weight_dense=1):

  return np.random.random(dense_layer_shape)**degree_weight_dernse


def softmax(input_matrix):

  total = np.nansum(np.exp(input_matrix))

  return np.exp(input_matrix)/total

def relu(input_matrix):
  input_matrix[input_matrix<0] = 0
  return input_matrix

def convolution2d(matrix, window, activation = "softmax", stride = 1):

  if window.shape[0] != window.shape[1]:
    return "The kernel have to be a square matrix"
  elif stride == 0:
    return "Stride must have to be > 0"

  s1,s2 = 0,0
  conv = np.zeros([int((matrix.shape[0]-
         window.shape[0])/stride +1),int((matrix.shape[1]
         - window.shape[1])/stride+1)])

  for i in range(conv.shape[0]-window.shape[0]):
    for j in range(conv.shape[1]-window.shape[1]):
      conv[i,j] = np.nansum(np.array([np.array(
                  [window[z][i2]*matrix[s2+z][s1+i2]
                  for i2 in range(window.shape[1])])
                  for z in range(window.shape[0])]))

      s1 = j+1+stride-1
    s2 = i+1+stride-1

  if activation == "softmax" or activation ==  "Softmax" or activation == "SOFTMAX":
    output = softmax(conv)
  elif activation == "relu" or activation == "ReLU" or activation == "ReLu" or activation == "RELU":
    output = relu(conv)
  elif activation == None or activation == "none" or activation == "NONE" or activation == "None":
    output = conv

  return output



def conv2d(matrix, kernels, activation = "softmax", stride =1):

  return np.array([convolution2d(matrix, window, activation = "softmax", stride = 1) for window in kernels])


def maxPool2D(output_convolution2d,shape = [2,2]):

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


def flatten(output_maxpool):

  return output_maxpool.flatten()


def dense(input_dense, weight_dense):

  if input_dense.shape != weight_dense.shape:
    return "Error: input_dense.shape and weight_dense.shape are not equal."
 
  return input_dense*weight_dense
    
def loss(input_, degree = 1):

  mean = np.nanmean(input_)

  return (1/len(input_))*np.nansum((input_ - mean)**degree)

