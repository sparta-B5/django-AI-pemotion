from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

modal_path = 'static/model/model.h5'
model = load_model(modal_path)

classes = {0: 'angry', 1: 'happy', 2: 'sad'}

def mainFunc(img_path):
    img_path = img_path.strip("/") 
    result = predict_emotion(img_path)
    return result

# user의 업로드 이미지로 예측
# img_path: 
def predict_emotion(img_path):
    image = load_img(img_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.array([image]) / 255

    # emotion 예측
    emotion_pred = model.predict(image)

    probability = emotion_pred[0]
    probability_max = probability.max()
    probability_index = probability.argmax()
    emotion_label = classes[probability_index]
    
    # 클라이언트에 보내줄 결과
    result = {
        'predict' : {value: probability[key] for key, value in classes.items()},
        'label':emotion_label,
        'percent': round(probability_max*100,2),
    }
    return result

