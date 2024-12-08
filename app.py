import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

# Load the pre-trained model
try:
    model = load_model("Custom_Structure_Animal_Classification_VGG16_v2.h5")
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Class names
class_names = ["Class 0", "Class 1", "Class 2", "Class 3"]  # Replace with actual names

# Function to preprocess images
def preprocess_image(image):
    img = image.resize((224, 224))  # Resize to VGG16 input size
    img_array = img_to_array(img) / 255.0  # Normalize the image
    return np.expand_dims(img_array, axis=0)

# Streamlit UI
st.title("Animal Classification App")
st.sidebar.header("Instructions")
st.sidebar.write("Upload an image of an animal to classify it.")

st.write("Upload an image of an animal to classify it!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file:
    try:
        # Load and preprocess image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        img_data = preprocess_image(image)

        # Make prediction
        prediction = model.predict(img_data)
        predicted_class = np.argmax(prediction, axis=1)
        confidence_scores = prediction[0]

        # Display result
        st.write(f"Predicted Class: {class_names[predicted_class[0]]}")
        st.write("Prediction Confidence Scores:")
        for i, score in enumerate(confidence_scores):
            st.write(f"{class_names[i]}: {score:.2f}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
