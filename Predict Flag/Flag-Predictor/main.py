# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 07:13:28 2021

@author: asus
"""

from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

model = load_model('keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

image = Image.open('austria6.jpg')
#try austria6.jpg, albania6.jpg, ukraine7.jpg

size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

data[0] = normalized_image_array

prediction = model.predict(data)
prediction = prediction[0]

i = np.where(prediction == np.amax(prediction))
index = i[0].tolist()

labels = open('labels.txt', 'r+')
list = labels.readlines()
print(list[index[0]])