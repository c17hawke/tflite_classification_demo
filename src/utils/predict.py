import os
import imghdr
import numpy as np
import sys
import cv2
import tensorflow.lite as tflite

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

def load_model(model_path):
    interpreter = tflite.Interpreter(model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    return interpreter, input_details, output_details

def resize_expand_img(input_img, input_details):
    _, pixel_ht, pexel_wd, _ = input_details[0]['shape']
    resized_img = cv2.resize(input_img, (pixel_ht, pexel_wd))
    expand_img = np.expand_dims(resized_img, 0)
    return expand_img

def prediction(config):
    img_path = config["predict"]["test_img_path"]
    model_path = os.path.join(config["train"]["model_file_dir"], "model.tflite")
    label_map = config["predict"]["label_map"]
    input_img = get_img(img_path)
    interpreter, input_details, output_details = load_model(model_path)
    input_img = resize_expand_img(input_img, input_details)

    # prediction
    input_index = input_details[0]['index']
    interpreter.set_tensor(input_index, input_img)
    interpreter.invoke()
    output_index = output_details[0]['index']
    output = interpreter.get_tensor(output_index)
    pred =  np.squeeze(output)

    argmax = np.argmax(pred)
    result = label_map[argmax]
    print(f"predicted: {result}")
    return result, argmax