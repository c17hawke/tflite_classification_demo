import os
import tensorflow as tf
from tflite_model_maker import image_classifier

def training_model(config):
    URL = config["train"]["base_url"]
    data_split = config["train"]["data_split"]
    model_file_dir = config["train"]["model_file_dir"]
    data_file_name = config["train"]["data_file_name"]
    data_dir = config["train"]["data_dir"]

    os.makedirs(model_file_dir, exist_ok=True)

    image_path = tf.keras.utils.get_file(
        data_file_name,
        f"{URL}{data_file_name}",
        extract=True, cache_dir=data_dir
    )
    image_path = os.path.join(
        os.path.dirname(image_path), data_file_name.split(".")[0]
    )
    
    data = image_classifier.DataLoader.from_folder(image_path)
    train, test = data.split(data_split)

    model = image_classifier.create(train)

    loss, accuracy = model.evaluate(test)

    print(loss, accuracy)

    model.export(export_dir=model_file_dir)
