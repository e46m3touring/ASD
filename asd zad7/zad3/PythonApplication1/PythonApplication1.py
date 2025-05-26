
import numpy as np

# 1. Zwykły blur (box blur 3x3)
def box_blur(image):
    rows, cols = image.shape
    result = np.copy(image)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            neighborhood = image[i-1:i+2, j-1:j+2]
            result[i, j] = np.mean(neighborhood)
    return result.astype(np.uint8)

# 2. Blur Gaussa (weighted blur 3x3)
def gaussian_blur(image):
    kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ])
    kernel = kernel / kernel.sum()

    rows, cols = image.shape
    result = np.copy(image)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            neighborhood = image[i-1:i+2, j-1:j+2]
            result[i, j] = np.sum(neighborhood * kernel)
    return result.astype(np.uint8)

# 3. Thresholding (czarno-białe przekształcenie)
def threshold_image(image, threshold):
    binary_image = np.where(image >= threshold, 1, 0)
    return binary_image

# Przykładowe użycie
if __name__ == "__main__":
    image = np.array([
        [10, 50, 80, 90, 100],
        [60, 80, 90, 100, 110],
        [90, 110, 120, 130, 140],
        [100, 120, 140, 150, 160],
        [110, 130, 150, 170, 180]
    ], dtype=np.uint8)

    print("Oryginalny obraz:")
    print(image)

    blurred = box_blur(image)
    print("\nPo box blur:")
    print(blurred)

    g_blurred = gaussian_blur(image)
    print("\nPo gaussian blur:")
    print(g_blurred)

    thresholded = threshold_image(image, 100)
    print("\nPo thresholding (prog=100):")
    print(thresholded)

