from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

file = r".\\Images\AEB.jpg"

img = Image.open(file)

r_values,g_values,b_values = img.split()

red_img = Image.merge('RGB', (r_values, g_values.point(lambda _: 0),b_values.point(lambda _: 0)))
green_img = Image.merge('RGB', (r_values.point(lambda _: 0), g_values,b_values.point(lambda _: 0)))
blue_img = Image.merge('RGB', (r_values.point(lambda _: 0), g_values.point(lambda _: 0),b_values))

mean_img = []
weight_img = []

for r,g,b in zip(r_values.getdata(),g_values.getdata(),b_values.getdata()):
   mean_img.append(int((r + g + b)/3))
   weight_img.append(int(0.299 * r + 0.587 * g + 0.114 * b))

fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(10, 10))

axes[0][0].imshow(img)
title = f'Original Image\nResolution: {img.width}x{img.height}'
axes[0][0].set_title(title)

axes[0][1].imshow(red_img)
title = f'Red Channel\nResolution: {red_img.width}x{red_img.height}'
axes[0][1].set_title(title)

axes[0][2].imshow(green_img)
title = f'Green Channel\nResolution: {green_img.width}x{green_img.height}'
axes[0][2].set_title(title)

axes[0][3].imshow(blue_img)
title = f'Blue Channel\nResolution: {blue_img.width}x{blue_img.height}'
axes[0][3].set_title(title)

mean_img = np.array(mean_img).reshape(-1,img.width)

axes[1][0].imshow(Image.fromarray(mean_img),cmap="gray")
title = f'Grayscale (Average)\nResolution: {img.width}x{img.height}'
axes[1][0].set_title(title)

weight_img = np.array(weight_img).reshape(-1,img.width)

axes[1][1].imshow(Image.fromarray(weight_img),cmap="gray")
title = f'Grayscale (Weight)\nResolution: {img.width}x{img.height}'
axes[1][1].set_title(title)

r_values = np.array(r_values).reshape(-1,img.width)

axes[1][2].imshow(Image.fromarray(r_values),cmap="gray")
title = f'Grayscale (Red Channel)\nResolution: {img.width}x{img.height}'
axes[1][2].set_title(title)

# Hide the axis
for ax in axes.flatten():
   ax.axis('off')

plt.subplots_adjust(hspace=0,top=0.5)
plt.show()