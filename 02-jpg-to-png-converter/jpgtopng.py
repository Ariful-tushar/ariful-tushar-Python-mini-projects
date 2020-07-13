import sys
import os
from PIL import Image

#Save the folder name where images are located
img_path = input("please give the folder name where images are located: ")   #sys.argv[1]

#Get the folder name to create it and save the converted files
new_path =  input ("please give the folder name where you want to save: ") #sys.argv[2]

def convertion(img_path, new_path):
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    for filesname in os.listdir("images"):
        img = Image.open(f'images/{filesname}')
        clean_name = os.path.splitext (filesname)[0]
        img.save(f"{new_path}/{clean_name}.png", 'png')

    print ("converted and saved to new folder")   
    
convertion(img_path,new_path)

