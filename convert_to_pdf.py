# Converts all images in a folder to a .PDF file

import os
from PIL import Image
from natsort import natsorted, ns

bookId = input("Enter the book id: ")

folderPath = f"./{bookId}/"

# Get all images in the folder
images = [file for file in os.listdir(folderPath) if file.endswith(('.png', '.jpg', '.jpeg'))]

# Natural sort the images by name
images = natsorted(images, alg=ns.IGNORECASE)

# Open images
imagesOpen = [Image.open(folderPath + image) for image in images]

# Create a new PDF file
pdf = imagesOpen[0]
pdf.save(folderPath + f"{bookId}.pdf", "PDF", resolution=100.0, save_all=True, append_images=imagesOpen[1:])

# Close the PDF file
pdf.close()