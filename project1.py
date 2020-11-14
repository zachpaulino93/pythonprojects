#!/usr/bin/env python3


"""
1. resize a image
2. rotate a Image
3. save image to a new folder in .jpeg format



1. arg argument to accept entire image folder?
2. loop through each image in that folder applying the changes
3.

from PIL import Image # Import Image class from the library.

image = Image.open("dstop.tiff") # Load the image.
rotated_image = image.rotate(180) # Rotate the image by 180 degrees.
rotated_image.save("file_rotated.png") # Save the rotated image.

"""

#os directory because folder is a directory not a file!

from PIL import Image
import os

def main():
    path = '/home/student-00-79bb12745b0f/images'
    for image_path in os.listdir(path):
        output_path = os.path(future path here)
        input_path = os.path.join(path, image_path)
        img = Image.open(input_path)
        print("Rotating image")
        rotated = img.rotate(-90) # .save(input_path + "_new.png")
        print("rotating complete")
        print()
        print("Scailing")
        scailing = rotated.resize((128,128))
        print("scailing completed")
        new_image = scailing.save(output_path + ".png")
        print("\n saving file")
        new_image.close
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
from PIL import Image
import os
import os.path
import shutil

def main():
    path = '/home/student-00-79bb12745b0f/images'
    output_path = '/opt/icons'
    for image_path in os.listdir(path):
        input_path = os.path.join(path, image_path)
        img = Image.open(input_path)
        print("Rotating image")
        rotated = img.rotate(-90)
        print("rotating complete")
        print()
        print("Scailing")
        scailing = rotated.resize((128,128))
        print("scailing completed")
        convert = scailing.convert('RGB')
        convert.save(output_path +"/" + image_path, 'jpeg')
        print("\n saving file")
       #  shutil.move(im_source, output_path)
        convert.close()
if __name__ == '__main__':
    main()
