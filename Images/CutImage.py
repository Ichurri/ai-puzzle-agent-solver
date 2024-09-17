from PIL import Image

def split_image_into_n_parts(image_path, n):
    image = Image.open(image_path)

    width, height = image.size

    part_width = width // n
    part_height = height // n

    cropped_images = []

    for i in range(n):
        for j in range(n):
            left = j * part_width
            top = i * part_height
            right = (j + 1) * part_width
            bottom = (i + 1) * part_height

            cropped_image = image.crop((left, top, right, bottom))

            cropped_images.append(cropped_image)
            cropped_image.save(f"image{i}_{j}.png")

    return cropped_images

image_path = input("Enter the image path: ") # tiger_image.jpg
n = int(input("Enter the number of parts (n) to split the image into n x n parts: ")) # 3

split_image_into_n_parts(image_path, n)