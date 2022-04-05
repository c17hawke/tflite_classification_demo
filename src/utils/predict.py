import os
import imghdr
import numpy as np
import sys
import cv2

def get_img(img_path):
    exist = os.path.join(img_path)
    img_type = imghdr.what(img_path)
    if (img_type not in ["jpeg", "png", "jpg"]) or (not exist) :
        print("quiting the program")
        sys.exit()
    else:
        print(f"yes the file is of type: {img_type}. proceeding further")
    
    img = cv2.imread(img_path)
    
    return img

def load_model():
    pass

def resize_expand_img():
    pass

def prediction(config):
    img_path = config["predict"]["test_img_path"]
    model_path = os.path.join(config["train"]["model_file_dir"], "model.tflite")
    label_map = config["predict"]["label_map"]
    input_img = get_img(img_path)
    interpreter = load_model()
    input_img = resize_expand_img()

