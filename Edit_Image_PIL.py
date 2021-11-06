"""Edit Image with PIL
"""

from PIL import Image, ImageFilter
from PIL import ImageEnhance

# Enhanced Image
img = Image.open('img.jpg')
img.show()
enh = ImageEnhance.Contrast(img)
enh.enhance(1.8).show("30% contract more")

# Change Image Typle
from PIL import Image
image = Image.open('img.jpg')
image.save('new_img.png')

# Resizing Image
from PIL import Image
img = Image.open('img.jpg')
new_img = img.resize((500, 500))
new_img.save('resize.jpg')
print(img.size) # Output: (1920, 1280)
print(new_img.size) # Output: (500, 500)

# Flipping image
img = Image.open('img.jpg')
img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flip.save('img_flip.jpg')
