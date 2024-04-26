#  Problem count 5: Today let's learn colvolution.
# Convolution is used in neural network and computer vision


import numpy as np

# At first make a matrix which will be convolved over another big matrix
# This matrix is called kernel
# A 3x3 kernel
window = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

# Now let's create another matrix.
# Window would be convolved over this matrix
matrix = np.random.randint(255, size = 2500).reshape([50,50])[:48,:48] # A 48x48 matrix


# Convolution with stride = 3
def convolution(matrix, window):
  s1,s2 = 0,0
  conv = np.zeros(matrix.shape)

  for i in range(int(matrix.shape[0]/window.shape[0]-1)):
    for j in range(int(matrix.shape[1]/window.shape[1]-1)):
      for z in  range(window.shape[0]):
        conv[s2+z,s1:s1+3] = np.array([window[z][i2]*matrix[s2][s1+i2] for i2 in range(window.shape[1])])

        s1 = (j+1)*3
      s2 = (i+1)*3

  return conv
# Now check if we were able to make the convolution
import matplotlib.pyplot as plt

conv = convolution(matrix,window)
plt.contourf(np.hstack([matrix,conv]), cmap = "gray")
plt.show()

# Now, let's try with a real image
matrix_ = plt.imread("drive/MyDrive/input.jpeg")
matrix = matrix_[0:165,0:297,0]


import matplotlib.pyplot as plt

conv = convolution(matrix,window)
plt.imshow(np.nanmean(matrix_[0:165,0:297,:], axis = 2), cmap = 'gray')
plt.show()
plt.imshow(conv, cmap = "gray")
