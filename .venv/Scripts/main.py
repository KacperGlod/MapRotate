import os
import random
from PIL import Image
import glob

# Ścieżka do folderu z obrazami
folder_path = 'C:\\Users\\Kacper\\Downloads\\Przycinanie\\before'

# Ścieżka do folderu zapisu przetworzonych obrazów
output_folder = 'C:\\Users\\Kacper\\Downloads\\Przycinanie\\after'
os.makedirs(output_folder, exist_ok=True)


# Funkcja do obracania i przycinania obrazu
def rotate_and_crop_image(image_path, output_path):
    with Image.open(image_path) as img:
        # Losowy kąt obrotu od 0 do 360 stopni
        angle = random.uniform(0, 360)
        rotated_img = img.rotate(angle, expand=True)

        width, height = rotated_img.size
        new_width, new_height = img.size

        # Współrzędne kadrowania
        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2

        cropped_img = rotated_img.crop((left, top, right, bottom))

        cropped_img.save(output_path)


for image_path in glob.glob(os.path.join(folder_path, '*.png')):
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    rotate_and_crop_image(image_path, output_path)

print("Przetwarzanie zakończone!")

