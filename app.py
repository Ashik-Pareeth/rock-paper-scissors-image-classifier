import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. Load the Trained Model ---
@st.cache(allow_output_mutation=True)
def load_model():
    # Load the model from the .keras file
    model = tf.keras.models.load_model('rock_paper_scissors_model.keras')
    return model

model = load_model()

# Define the class names in the correct order
class_names = ['paper', 'rock', 'scissors']

# --- 2. Set up the Streamlit Interface ---
st.title("Rock, Paper, Scissors - Image Classifier ✊✋✌️")
st.write("Upload an image of your hand, and the model will predict your move!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # --- 3. Preprocess the User's Image ---
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Resize the image to 160x160 as the model expects
    image = image.resize((160, 160))
    image_array = np.array(image)
    
    # Add a batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # --- 4. Make a Prediction ---
    prediction = model.predict(image_array)
    score = tf.nn.softmax(prediction[0])
    
    predicted_class = class_names[np.argmax(score)]
    confidence = 100 * np.max(score)

    # --- 5. Display the Result ---
    st.success(f"Prediction: {predicted_class.capitalize()}")
    st.info(f"Confidence: {confidence:.2f}%")