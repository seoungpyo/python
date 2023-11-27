import numpy as np
import matplotlib.pyplot as plt

def julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter):
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    img = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        Z = Z**2 + c
        mask = np.abs(Z) < 1000
        img += mask

    return img

def plot_julia_set(img):
    plt.imshow(img, cmap='twilight', extent=(-2, 2, -2, 2))
    plt.colorbar()
    plt.title('Julia Set')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

if __name__ == "__main__":
    width, height = 800, 800
    x_min, x_max = -2, 2
    y_min, y_max = -2, 2
    c = complex(-0.7, 0.27015)  # You can experiment with different values of c
    max_iter = 100

    julia_img = julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter)
    plot_julia_set(julia_img)
