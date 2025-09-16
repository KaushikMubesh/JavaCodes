import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load grayscale image
img = Image.open('image.jpg').convert('L')
img_matrix = np.array(img)

# SVD function
def svd_compress(img_matrix, k):
    U, S, VT = np.linalg.svd(img_matrix, full_matrices=False)
    S_k = np.zeros((k, k))
    np.fill_diagonal(S_k, S[:k])
    return np.dot(U[:, :k], np.dot(S_k, VT[:k, :]))

# Apply SVD repeatedly
def apply_svd_multiple_times(img_matrix, k, times):
    compressed = img_matrix.copy()
    for _ in range(times):
        compressed = svd_compress(compressed, k)
    return compressed

# Parameters
k = 50       # Number of singular values to keep
times = 3   # How many times to apply SVD

# Run compression
final_img = apply_svd_multiple_times(img_matrix, k, times)

# Show result
plt.figure(figsize=(10,4))
plt.subplot(1, 2, 1)
plt.imshow(img_matrix, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(final_img, cmap='gray')
plt.title(f"SVD applied {times} times (k={k})")
plt.axis('off')

plt.show()
