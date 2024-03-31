import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from PIL import Image 

loaded_model = load_model("emotion_detection_model.h5") #load model

def predict_image(input_img):
    # Preprocessing
    resized_image = cv2.resize(input_img, (400, 400))
    img_array = img_to_array(resized_image) 
    img_array = np.expand_dims(img_array, axis= 0)  
    # predict
    predictions = loaded_model.predict(img_array)
    predicted_class = np.argmax(predictions)
    class_names = ['sad', 'unemotional', 'angry', 'happy'] 
    return class_names[predicted_class]