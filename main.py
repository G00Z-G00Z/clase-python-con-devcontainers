import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0, 2 * np.pi , 2 * np.pi / 100)
y = np.sin(theta)

plt.plot(theta,y)
plt.grid(True)

# plt.show() doesnt display the image. Maybe a different port??
# plt.show()

# Workaround to save the plot into  an image
plt.savefig("figura")


