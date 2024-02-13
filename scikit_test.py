from sklearn import datasets

digits = datasets.load_digits()

import matplotlib.pyplot as plt

plt.matshow(digits.images[0], cmap="Greys")
plt.show()
