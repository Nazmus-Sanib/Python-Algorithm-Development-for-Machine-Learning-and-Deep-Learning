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
  print(conv.shape)

  for i in range(conv.shape[0]-window.shape[0]):
    for j in range(conv.shape[1]-window.shape[1]):
      conv[i,j] = np.nansum(np.array([np.array(
                  [window[z][i2]*matrix[s2+z][s1+i2]
                  for i2 in range(window.shape[1])])
                  for z in range(window.shape[0])]))

      s1 = j+1+stride-1
    s2 = i+1+stride-1

  if activation == "softmax":
    output = softmax(conv)
  elif activation == "relu":
    output = relu(conv)

  return output
