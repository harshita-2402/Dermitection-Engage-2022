<h1 align = "middle"> Derm(i)tection (Microsoft Engage '22) </h1>
<h3 align = "middle"> Real time disease detection web-application made during Microsoft Engage '22 mentorship program. </h3>
<h3 align = "middle"> <a href =https://youtu.be/GQsi631Xc_c> See Demo Video</a> </h3>

<p align="middle">
  <img src="/media/logo1.JPG" width="300" />
  <img src="/media/logo2.JPG" width="400" />
 </p>

## TABLE OF CONTENTS
- [About the Project](#heading1)
  * [Diseases Covered](#subheading1)
  * [Data](#subheading2)
  * [Tech Stack](#subheading3)
  * [Compatible Platforms](#subheading4)
- [UI of the Webapp](#heading2)
- [How to setup and run](#heading3)
- [Additional Instructions](#heading4)




![img](https://www.gene.com/assets/content/tile_image/C3bTJ6vzY5zW4cAPwgUUjmZHFr4TgXLk.jpg)

## **ABOUT THE PROJECT** <a name="heading1"></a>
Dermitection is a web application for disease detection. The webapp helps in quick and remote diagnosis of diseases in real time!
This web-app is part of the Microsoft Engage 2022 mentorship program.

Dermitection uses deep learning for disease recognition covering 6 types of common skin diseases and 5 types of diseases related to eyes in humans. Haaracascades for eye and face are used for detecting eye and facial regions of interest for detection in real time.

Details of the detected disease like Name of disease, Symptoms and Cure/Remedies are displayed from the database as well.

### **DISEASES COVERED** <a name="subheading1"></a>
* Skin Based:
  - Acne and Rosacea
  - Eczema
  - Light diseases and disorders of Pigmentation
  - Melanoma
  - Vascular Tumors
  - Warts Molluscum and other Viral Infections
* Eye Based:
  - Bulging Eyes
  - Cataracts
  - Crossed Eyes
  - Glaucoma
  - Uveitis
 ### **DATA** <a name="subheading2"></a>
 
 Datasets used taken from [Kaggle](https://www.kaggle.com/) and self aquired:
 
   - https://www.kaggle.com/datasets/shubhamgoel27/dermnet (SKIN)
   - https://www.kaggle.com/datasets/kondwani/eye-disease-dataset (EYE)
    
    
### **TECHNOLOGY USED** <a name="subheading3"></a>
- Python
- Django
- Tensorflow Keras (Convolutional Neural Network, InceptionV3)
- OpenCV
- HTML/CSS/JavaScript
- Bootstrap
- Sqlite Database

### **COMPATIBLE PLATFORMS** <a name="subheading4"></a>
This web-application is compatible with Laptops, PCs and Tablets.

## **UI OF THE WEBSITE** <a name="heading2"></a>
<p align="middle">
  <img src="/media/img1.JPG" width="300" />
  <img src="/media/img2.JPG" width="300" /> 
</p>
<p align="middle">
  <img src="/media/img3.JPG" width="600" />
  <img src="/media/img4.JPG" width="700" /> 
</p>

## **HOW TO SETUP AND RUN** <a name="heading3"></a>
- Clone the GitHub repository: 
``` sh
$ git clone [https://github.com/harshita-2402/Dermitection-Engage-22.git](https://github.com/harshita-2402/Dermitection-Engage-2022.git)
```
- Download the required models:

  * Skin model: https://drive.google.com/file/d/1XKhezpc23ZqHpHTQtLaeYBwxIQm5bCfT/view?usp=sharing
  
  * Eye model: https://drive.google.com/file/d/108Gq_0j0wssfIVA-3vUsgPj_kN4zAkoy/view?usp=sharing
  
  And place them inside FaceRecog folder

- Install dependencies from requirements.txt using command 
``` sh
$ pip install -r requirements.txt
```
- Open Powershell or CMD terminal if using Windows, in the directory containing "FaceRecog" set-up the Django server by running the following command.
``` sh
$ python manage.py runserver
```

- Open up Google Chrome and type in ```localhost:8000\```. 
- Click on 'DISEASE-DETECTION' on the nav-bar or scroll down and click on 'Start Detection' for eye or skin disease identification.

***Dermitection is up and running!***

## **ADDITIONAL INSTRUCTIONS:** <a name="heading4"></a>
1. The Deep Learning models load faster with a GPU, if GPU is not available please wait for about 1-2 minutes for the app to start and ignore CPU/GPU related warnings.
2. The Jupyter Notebooks in modelTraining folder can be used to train the disease detection models again.

