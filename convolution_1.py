
import numpy as np

# At first make a matrix which will be convolved over another big matrix
# This matrix is called kernel
# A 3x3 kernel
window = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

# Now let's create another matrix.
# Window would be convolved over this matrix
matrix = np.random.randint(255, size = 2500).reshape([50,50])[:48,:48] # A 48x48 matrix


# Convolution
def convolution(matrix, window):

  if window.shape[0] != window.shape[1]: return "The kernel have to be a square matrix"

  stride = window.shape[0]

  s1,s2 = 0,0
  conv = np.zeros(matrix.shape)

  for i in range(int(matrix.shape[0]/window.shape[0]-1)):
    for j in range(int(matrix.shape[1]/window.shape[1]-1)):
      for z in  range(window.shape[0]):
        conv[s2+z,s1:s1+window.shape[1]] = np.array([window[z][i2]*matrix[s2][s1+i2] for i2 in range(window.shape[1])])

        s1 = (j+1)*stride
      s2 = (i+1)*stride

  return conv
# Now check if we were able to make the convolution
import matplotlib.pyplot as plt

conv = convolution(matrix,window)
plt.contourf(np.hstack([matrix,conv]), cmap = "gray")
plt.show()

# Now, let's try with a real image
matrix_ = plt.imread("drive/MyDrive/input.jpeg")

import matplotlib.pyplot as plt


plt.imshow(np.nanmean(matrix_, axis = 2), cmap = 'gray')
plt.show()

window = np.array([[1,2,1,1,2,1,1],[0,0,0,0,0,0,0],[-1,-2,-1,-1,-2,-1,-2],[1,2,1,1,2,1,1],[0,0,0,0,0,0,0],[-1,-2,-1,-1,-2,-1,-2],[1,2,1,1,2,1,1]])

# A code for adapting the matrix shape with the windows shape
for i in range(3,7):
  
  matrix = matrix_[:matrix_.shape[0] - matrix_.shape[0]%(i+1),:matrix_.shape[1]- matrix_.shape[1]%(i+1),0]

  conv = convolution(matrix,window[:i,:i])

  plt.imshow(conv, cmap = "gray")
  plt.show()
