import streamlit as st
import nbformat
from nbconvert import PythonExporter
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

# Function to execute the Jupyter Notebook
def execute_notebook(notebook_path):
    """
    Executes a Jupyter notebook and extracts the model created within.
    """
    try:
        # Convert Jupyter notebook to Python script
        exporter = PythonExporter()
        python_script, _ = exporter.from_filename(notebook_path)

        # Execute the Python script
        exec(python_script, globals())
        st.success("Jupyter Notebook executed successfully!")
        return globals().get('model')  # Expect 'model' variable in the notebook
    except Exception as e:
        st.error(f"Error executing Jupyter Notebook: {e}")
        st.stop()

# Define notebook path
notebook_path = "/Users/EliseZamora_1/Documents/School/Education/Animal_Classification_Project/Assignment 3/DeployingAIA3/Custom_Structure_Animal_Classification_VGG16_v3.ipynb"

if not os.path.exists(notebook_path):
    st.error(f"Notebook not found at path: {notebook_path}")
    st.stop()

st.info("Executing the Jupyter Notebook...")
model = execute_notebook(notebook_path)

# Class names
class_names = ["Red Fox", "Black Bear", "Beaver", "Mink"]  # Replace with actual class labels from the notebook

# Function to preprocess images
def preprocess_image(image):
    img = image.resize((224, 224))  # Resize to VGG16 input size
    img_array = img_to_array(image) / 255.0  # Normalize the image
    return np.expand_dims(img_array, axis=0)

# Streamlit App Interface
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
