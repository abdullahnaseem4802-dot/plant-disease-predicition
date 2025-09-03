# 🌱 Plant Disease Prediction App  

A **deep learning-based web application** built with **TensorFlow/Keras** and **Streamlit** that predicts plant leaf diseases from uploaded images.  
This project is designed to help farmers, researchers, and students quickly detect plant health issues using computer vision.  

---

## 📊 Dataset  

The model was trained on the [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease) from Kaggle.  
It contains **50,000+ labeled leaf images** of different plant species and their diseases.  

👉 To use the dataset:  
1. Download it from Kaggle.  
2. Extract it inside your project folder (e.g., `data/`).  
3. Organize it in subfolders like this:  



## Quick Start (Local)

1) **Create & activate a virtual environment (Windows):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

2) **Install dependencies:**
```bash
pip install -r requirements.txt
```


3) **Run the Streamlit app:**
```bash
streamlit run app/app.py
```

## Project Structure
```

plant-disease-prediction/
│── app.py                # Streamlit web app
│── plant_disease_model.h5  # Pre-trained model
│── requirements.txt       # Dependencies
│── data/                  # Dataset (Kaggle PlantVillage)
│── README.md              # Project documentation


Author
```
 Abdullah Naseem

 ```



