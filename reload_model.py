from tensorflow.keras.models import load_model

# Load the model
model = load_model("Custom_Structure_Animal_Classification_VGG16_v2.h5")
print("Model loaded successfully!")

# Re-save the model
model.save("Custom_Structure_Animal_Classification_VGG16_v2_revised.h5")
print("Model re-saved successfully as 'Custom_Structure_Animal_Classification_VGG16_v2_revised.h5'")
