import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image,ImageOps
import numpy as np


def classify(image,model,class_names):
    # convert image to (244,244) # it is default for teachable machines
    image = ImageOps.fit(image,(224,224),Image.Resampling.LANCZOS)

    # convert image into numpy array
    image_array = np.asarray(image)

    # normalize the image convert it into (-1 or 1)
    normalized_img_array = image_array.astype(np.float32)/127.5 -1

    # set the model input
    data = np.ndarray(shape=(1,224,224,3),dtype=np.float32)
    data[0] = normalized_img_array

    # make predictions
    prediction = model.predict(data)
    # index = np.argmax(prediction)
    index = 0 if prediction[0][0] > 0.95 else 1
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name,confidence_score

# set title
st.title("Pneumonia Classifier")

# set header
st.header("Please upload a chest X-Ray image")

# upload file
file = st.file_uploader("Upload a image", type=['jpeg','jpg','png'])

# load classifier
model = load_model("keras_model.h5")

# load class_names
with open("labels.txt","r") as f:
    class_names = [a[:-1].split(" ")[1] for a in f.readlines()]
    f.close()

# display the image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image,use_column_width=True)

    # classify the image
    class_name,conf_score = classify(image,model,class_names)

    # write classification
    st.write(f"## {class_name}")
    st.write(f"### Score:{conf_score}")



