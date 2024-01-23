


#final code
import rasterio as rio
import math
import cv2
from PIL import Image, ImageOps
import numpy as np
from patchify import patchify
import os 
import time

def clip_overlap_image_pixlewise(image_folder, patch_size ,save_folder):
    t1 = time.time()
    dir_list = os.listdir(image_folder)
    for file in dir_list:
        image = (image_folder + "\\" + file)
        img = cv2.imread(image)D:\try4

        img_height = img.shape[0]#height
        img_width = img.shape[1]#width
# giving perfect h and w to cut exactly as patch size

        new_h = patch_size * (math.ceil(img_height/patch_size))#math.ceil for next exit number
        new_w = patch_size * (math.ceil(img_width/patch_size))
# creating new h and w for padding the image(padding means extra zero pixles blck img)
        padding_w = new_w - img.shape[1]
        padding_h = new_h - img.shape[0]
        
        padding = (0,0,padding_w,padding_h)### 0,0 use for 1at 0 for top of the image & 2nd zero for left of the image
        open_img = Image.open(image)
        padding_image = ImageOps.expand(open_img, padding)###use for expanding image
        im = np.asarray(padding_image)
#         patches = patchify(im, (patch_size, patch_size, 3), step = patch_size//2) ###//2 is use for 50% overlap image 
#         patches = patchify(im, (patch_size, patch_size, 3), step = 384 )
        patches = patchify(im, (patch_size, patch_size, 3), step = 512)
        for i in range(patches.shape[0]):
            for j in range(patches.shape[1]):
                patch = patches[i,j,0]
                patch = Image.fromarray(patch)
                num = str(i * patches.shape[1] + j)

                name = file.split(".jpg")[0]
                abc = save_folder + '\\' + name + "_" + num +".png"
                patch.save(abc)
                print(abc)
        t2 = time.time()
        print('time taken =', t2-t1)

image_folder = input('image_folder: ')
patch_size = int(input('patch size of clip image: '))
save_folder = str(input('save image folder: ')) 
clip_overlap_image_pixlewise(image_folder,patch_size, save_folder)