from .models import Disease
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model


class_names_eye = ['Bulging', 'Cataracts', 'Crossed Eye', 'Glaucoma', 'No disease', 'Uveitis']
class_names_skin = ['Acne and Rosacea Photos', 'Eczema Photos',
    'Light Diseases and Disorders of Pigmentation',
    'Melanoma Skin Cancer Nevi and Moles',  'Vascular Tumors',
    'Warts Molluscum and other Viral Infections', 'No Diseases']

eyemod = load_model('eye_disease.h5')
dismod = load_model('disClass.h5')

np.set_printoptions(suppress=True)

eye_detect = cv2.CascadeClassifier('haarcascade_eye.xml')
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class DiseaseDetect():
    def __init__(self):
        mode = ""
    def convertToRGB(self, image):
            return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    def predict(self, model, img):
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        id = np.argmax(predictions[0])
        if model == eyemod:
            predicted_class = class_names_eye[id]
            return predicted_class, id+8
        else:
            predicted_class = class_names_skin[id]
            return predicted_class, id+1
        # confidence = round(100 * (np.max(predictions[0])), 2)
        return predicted_class, id+1

    def detect_eyedisease(self):    

        source = cv2.VideoCapture(0)
        while 1:
            not_to_use, image = source.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_detect.detectMultiScale(gray, 1.3, 2)
            for (x,y,w,h) in faces:
                face_roi = gray[y:y+w, x:x+h]
                color = image[y:y+w, x:x+h]
                image1 = cv2.resize(image, (224, 224))
                normalized_image = image1/255
                eyes = eye_detect.detectMultiScale(face_roi, 1.5, 1)
                resized_image = cv2.resize(color, (224, 224))
                normalized_image = resized_image/255
                for (ex, ey, ew, eh) in eyes:
                    result, id = self.predict(eyemod, normalized_image)
                    print(result, id)
                    cv2.rectangle(color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                    cv2.putText(color,str(result), (ex, ey), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    x = self.fetch_details(id)
            cv2.imshow('Dermitection!', image)
            key = cv2.waitKey(1)
            if key == 27:
                break
            
        cv2.destroyAllWindows()
        source.release()
        return x

    def detect_disease(self):    

        source = cv2.VideoCapture(0)
        while 1:
            not_to_use, image = source.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_detect.detectMultiScale(gray, 1.3, 2)
            for (x,y,w,h) in faces:
                face_roi = gray[y:y+w, x:x+h]
                color = image[y:y+w, x:x+h]
                image1 = cv2.resize(color, (224, 224))
                normalized_image = image1/255
                result, id = self.predict(dismod, normalized_image)
                print(result, id)
                cv2.rectangle(color, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(color,str(result), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                x = self.fetch_details(id)    

            cv2.imshow('Dermitection!', image)
            key = cv2.waitKey(1)
            if key == 27:
                break
            
        cv2.destroyAllWindows()
        source.release()
        return x
    
    def fetch_details(self, id: str):
        disease = Disease.objects.get(id = id)
        name = disease.disease_name
        symptoms = disease.symptoms
        cure = disease.cure
        details = str(name + '\n' + symptoms + '\n' + cure)
        return details