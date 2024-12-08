from tensorflow.keras.models import load_model

# Load the model
try:
    model = load_model("Custom_Structure_Animal_Classification_VGG16_v2.h5")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Failed to load model: {e}")
