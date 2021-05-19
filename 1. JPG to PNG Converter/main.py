import sys
import re
import os
from PIL import Image

ref_folder = sys.argv[1]
new_folder = sys.argv[2]

def generate_folder(new_folder):
    try:
        os.mkdir("./"+new_folder)
    except:
        print("Folder already exists!")
        return "Folder already exists!"

def get_file_name(image):
    raw_file_name = image.filename
    pattern = re.compile(r"\.(\/[a-zA-Z0-9]+\/)([a-zA-Z0-9]+)(\.jpg|\.jpeg)")
    return pattern.match(raw_file_name).group(2)

def transform_and_save_image(image,file_name):
    if(image.format=="JPEG"):
        image.save("./"+new_folder+"/"+file_name+".png")

generate_folder(new_folder)
files = os.listdir("./Pokedex")
for picture in files:
    pattern = re.compile(r"(.+)(\.jpg$)")
    if(pattern.match(picture)!=None):
        img = Image.open("./"+ref_folder+"/"+picture)
        name = get_file_name(img)
        transform_and_save_image(img,name)