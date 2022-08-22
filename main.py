import numpy as np
import matplotlib.pyplot as plt

# Codigo de la clase
theta = np.arange(0, 2 * np.pi , 2 * np.pi / 100)
y = np.sin(theta)
y2 = np.cos(theta)
plt.plot(theta,y, "*r", linewidth=5)
plt.plot(theta,y2, "ob", linewidth=10)
plt.grid(True)
plt.title("Seno de un angulo")
plt.legend([r"sin($\theta$)", r"cos($\theta$)"])
plt.ylabel(r"y = sin($\theta$)")
plt.xlabel(r"$\theta$")

# plt.show() doesnt display the image. Maybe a different port??
plt.show()

# Workaround to save the plot into  an image
plt.savefig("figura")


