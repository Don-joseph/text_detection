import cv2
import easyocr
# import matplotlib.pyplot as plt
import pyttsx3
import streamlit as st
from PIL import Image
import numpy as np

st.title("TEXT DETECTION")
st.header("please upload a PIC")
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

if file is not None:
    img = Image.open(file).convert('RGB')
    st.image(img, use_column_width=True)

    # Convert Image to NumPy array
    img_np = np.array(img)

    # Instance text detector
    reader = easyocr.Reader(['en'], gpu=False)

    # Detect
    text_dt = reader.readtext(img_np)
    s = []
    k=""
    for t in text_dt:
        print(t)

        bbox, text, confi = t
        s.append(text)
        k+=text+" "
        cv2.rectangle(img_np, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(img_np, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 0, 0), 2)

    st.image(img_np, caption='Annotated Image', use_column_width=True)
    st.write("Extracted Text:", k)


    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)
    for text_to_speak in s:
        # Convert the text to speech
        engine.say(text_to_speak)
    engine.say(k)
    engine.runAndWait()

    # Close the Image object
    img.close()
