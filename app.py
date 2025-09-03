import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# ✅ Load the pre-trained full model
@st.cache_resource
def get_model():
    model = load_model("plant_disease_model.h5")
    return model

model = get_model()

def preprocess_image(image):
    img = Image.open(image).convert("RGB")  # ✅ use RGB not L
    img = img.resize((224,224))
    img = np.array(img)
    img = np.expand_dims(img, axis=0)   # (1,224,224,3)
    img = img / 255.0
    return img



# ✅ Streamlit UI
st.title("🌿 Plant Disease Prediction App")

uploaded_file = st.file_uploader("Upload a plant leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Leaf", use_column_width=True)

    img_array = preprocess_image(uploaded_file)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction, axis=1)[0]

    # ⚠️ Make sure this matches the same order you used during training
    class_names = [
        "Pepper__bell___Bacterial_spot",
        "Pepper__bell___healthy",
        "Potato___Early_blight",
        "Potato___Late_blight",
        "Potato___healthy",
        "Unknown_or_Dropped"  # extra placeholder
    ]

    st.write(f"**Prediction:** {class_names[class_idx]}")

    st.write("🔹 Raw Prediction Probabilities:")
    st.write(prediction)
    st.write("🔹 Predicted Class Index:", class_idx)
