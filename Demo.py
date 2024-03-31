import gradio as gr
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from PIL import Image 

loaded_model = load_model("") # Tên của model đã lưu dưới định dạng h5.

def classify_image(input_img):
    
    resized_image = cv2.resize(input_img, (400, 400))
    img_array = img_to_array(resized_image)  # Chuyển đổi ảnh thành numpy array
    img_array = np.expand_dims(img_array, axis= 0)  # Thêm chiều batch
    
    predictions = loaded_model.predict(img_array)
    predicted_class = np.argmax(predictions)
    class_names = ['sad', 'unemotional', 'angry', 'happy'] # Tương ứng 0,1,2,3
    return class_names[predicted_class]

demo = gr.Interface(classify_image, gr.Image(), "text")
if __name__ == "__main__":
    demo.launch()