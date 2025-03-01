from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load the image
file = r".\\Images\AEB.jpg"
img = Image.open(file)

# Convert image to NumPy array
img_array = np.array(img)

# Extract RGB channels
r_values, g_values, b_values = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]

# Create grayscale images
mean_img = np.mean(img_array, axis=2).astype(np.uint8)
weight_img = (0.299 * r_values + 0.587 * g_values + 0.114 * b_values).astype(np.uint8)

# Create RGB channel images
red_img = np.zeros_like(img_array)
green_img = np.zeros_like(img_array)
blue_img = np.zeros_like(img_array)

red_img[:, :, 0] = r_values
green_img[:, :, 1] = g_values
blue_img[:, :, 2] = b_values

# Convert back to Image objects
red_img_pil = Image.fromarray(red_img)
green_img_pil = Image.fromarray(green_img)
blue_img_pil = Image.fromarray(blue_img)
mean_img_pil = Image.fromarray(mean_img)
weight_img_pil = Image.fromarray(weight_img)
r_values_pil = Image.fromarray(r_values)

# Plot images
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(10, 10))

# Original image
axes[0][0].imshow(img)
axes[0][0].set_title(f'Original Image\nResolution: {img.width}x{img.height}')

# RGB channel images
axes[0][1].imshow(red_img_pil)
axes[0][1].set_title(f'Red Channel\nResolution: {img.width}x{img.height}')

axes[0][2].imshow(green_img_pil)
axes[0][2].set_title(f'Green Channel\nResolution: {img.width}x{img.height}')

axes[0][3].imshow(blue_img_pil)
axes[0][3].set_title(f'Blue Channel\nResolution: {img.width}x{img.height}')

# Grayscale images
axes[1][0].imshow(mean_img_pil, cmap="gray")
axes[1][0].set_title(f'Grayscale (Average)\nResolution: {img.width}x{img.height}')

axes[1][1].imshow(weight_img_pil, cmap="gray")
axes[1][1].set_title(f'Grayscale (Weight)\nResolution: {img.width}x{img.height}')

axes[1][2].imshow(r_values_pil, cmap="gray")
axes[1][2].set_title(f'Grayscale (Red Channel)\nResolution: {img.width}x{img.height}')

# Hide the last subplot
axes[1][3].axis('off')

# Hide axes
for ax in axes.flatten():
    ax.axis('off')

plt.subplots_adjust(hspace=0, top=0.5)
plt.show()