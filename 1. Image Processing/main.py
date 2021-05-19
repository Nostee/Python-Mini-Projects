from PIL import Image, ImageFilter

img = Image.open("./Pokedex/4.4 pikachu.jpg")

filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save("blur.png","png")