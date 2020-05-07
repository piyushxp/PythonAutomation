import sys
import os
from PIL import Image

#grab 1st and 2nd arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]



#check if new exists,if not create a new one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


#loop
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
     #To pick the firstpart, that is the name of the File
    clean_name= os.path.splitext(filename)[0]
    #To save the image 
    img.save(f"{output_folder}{filename}.png","png")
    print(f"{filename} done!")




#THE COMMAND TO USE:
#use this command in CLI to convert the JPG format Images in the folder SOURCE to png FORMAT
""" python3 JPGtoPNGConvertor.py Source/ new/  
Here Source is the Folder that contains JPG files and new is the Name of Folder that is Created,where the PNG converted Files are dumped""" 


#save

