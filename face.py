#!/usr/bin/python
# -*- coding: UTF-8 -*-
  
# face_detect.py
  
# Face Detection using OpenCV. Based on sample code from:
# http://www.pythontab.com
  
# Usage: python face_detect.py
  
import sys, os
#引入opencv库中的相应组件
from cv2.cv import *
#引入PIL库
from PIL import Image, ImageDraw
from math import sqrt
  
def detectObjects(image):
    #首先把图片转换为灰度模式，以便找到人脸位置
    grayscale = CreateImage(GetSize(image), 8, 1)
    CvtColor(image, grayscale, CV_BGR2GRAY)
  
    storage = CreateMemStorage(0)

    cascade = Load('haarcascade_frontalface_default.xml') 
    faces = HaarDetectObjects(grayscale, cascade, storage, 1.1, 2,
            CV_HAAR_DO_CANNY_PRUNING, (0, 0))
  
    result = []
    for f in faces:
        result.append(f[0])
    return result
  
def grayscale(r, g, b):
    return int(r * .3 + g * .59 + b * .11)
  
def process(infile, outfile):
  
    image = LoadImage(infile);
    if image:
        faces = detectObjects(image)
  
    im = Image.open(infile)
  
    if faces:
        draw = ImageDraw.Draw(im)
        print faces
        for f in faces:
            draw.rectangle(f, outline=(255, 0, 255))
  
        im.save(outfile, "JPEG", quality=100)
    else:
        print "Error: cannot detect faces on %s" % infile
  
if __name__ == "__main__":
    process('input.jpg', 'output.jpg')
