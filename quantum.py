import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ---------------------------
# 1. Load image and convert to grayscale
# ---------------------------
img = Image.open('image.jpg').convert('L')  # 'L' means grayscale
img_matrix = np.array(img)

print("Original Image Shape:", img_matrix.shape)

# Show Original Image
plt.figure(figsize=(5, 5))
plt.imshow(img_matrix, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

# ---------------------------
# 2. Print Original Matrix (Sample)
# ---------------------------
print("\nOriginal Image Matrix (10x10 sample):")
print(img_matrix[:10, :10])

# ---------------------------
# 3. Perform SVD
# ---------------------------
U, S, Vt = np.linalg.svd(img_matrix, full_matrices=False)
Sigma = np.diag(S)

print("\nShapes:")
print("U shape:", U.shape)
print("Sigma shape:", Sigma.shape)
print("Vt shape:", Vt.shape)

# ---------------------------
# 4. Show matrix samples
# ---------------------------
print("\nU Matrix (10x10 sample):")
print(U[:10, :10])

print("\nFirst 10 Singular Values (Σ):")
print(S[:10])

print("\nVᵀ Matrix (10x10 sample):")
print(Vt[:10, :10])

# ---------------------------
# 5. Visualize U, Σ, Vᵀ as heatmaps
# ---------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(U, cmap='viridis')
axes[0].set_title('U Matrix')
axes[0].axis('off')

axes[1].imshow(Sigma, cmap='viridis')
axes[1].set_title('Σ (Sigma)')
axes[1].axis('off')

axes[2].imshow(Vt, cmap='viridis')
axes[2].set_title('Vᵀ Matrix')
axes[2].axis('off')

plt.suptitle("SVD Decomposition Heatmaps")
plt.show()

# ---------------------------
# 6. Reconstruct Image using top k singular values
# ---------------------------
def reconstruct_image(k):
    Uk = U[:, :k]
    Sk = Sigma[:k, :k]
    Vk = Vt[:k, :]
    return np.dot(Uk, np.dot(Sk, Vk))

k_values = [5, 20, 50, 100]
plt.figure(figsize=(12, 6))

for i, k in enumerate(k_values, 1):
    compressed_img = reconstruct_image(k)
    plt.subplot(1, len(k_values), i)
    plt.imshow(compressed_img, cmap='gray')
    plt.title(f"k = {k}")
    plt.axis('off')

plt.suptitle("Image Compression using SVD")
plt.show()
