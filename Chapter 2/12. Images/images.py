import os
import zipfile
from PIL import Image
import numpy as np
import pandas as pd
from matplotlib.pyplot import imshow


train_path = 'mnistasjpg/trainingSet/trainingSet/'
test_path = 'mnistasjpg/testSet/testSet/'
train_folders = os.listdir(train_path)
test_folders = os.listdir(test_path)

for p in train_folders:
    p_img = os.listdir(train_path+p)

print(p_img[0])

def showImage(img,type='img'):
    if type == img:
        img = Image.open(img, 'r')
        img.show()

showImage(r'C:\Users\Asus\Documents\Education\Strive School\AI-Engineering\Chapter 2\12. Images\mnistasjpg\trainingSet\trainingSet\0\img_1.jpg')
