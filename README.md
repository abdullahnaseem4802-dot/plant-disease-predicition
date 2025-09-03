# 🌱 Plant Disease Prediction App  

This project is a **web-based application** that predicts plant leaf diseases using a **deep learning model** trained on the **PlantVillage dataset**. Users can upload an image of a plant leaf, and the app will classify it into the correct disease/healthy category.  

---

## **Features**  

* **Image Upload:** Upload `.jpg`, `.jpeg`, or `.png` leaf images.  
* **Deep Learning Predictions:** Classify images into multiple plant disease categories.  
* **Confidence Scores:** Display probability scores for predictions.  
* **User-friendly Interface:** Built with Streamlit for a clean and interactive UI.  

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



