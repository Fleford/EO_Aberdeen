import numpy as np
import matplotlib.pyplot as plt

# Load heads for surface
surf = np.loadtxt("EO_Aberdeen/Supply2_PotenSurf.txt")
surf = surf.reshape(25, 30)
plt.contour(surf)
plt.show()
print(surf)
