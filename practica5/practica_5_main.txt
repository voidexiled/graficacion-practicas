import numpy as np
import matplotlib.pyplot as plt

height, width = 100, 300
image = np.zeros((height, width, 3), dtype=np.uint8)


image[:, :100] = [255, 0, 0]
image[:, 100:200] = [0, 255, 0]
image[:, 200:] = [0, 0, 255]

plt.imshow(image)
plt.axis("off")
plt.title("Colores primarios en RGB")
plt.show()
