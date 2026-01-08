import streamlit as st
import numpy as np
import joblib
import request
import to

st.set_page_config(page_title="Handwriten Digit Recognition")
st.title("Handwriten Digit Recognition")
st.write("Upload Handwriten Digit and AI will try to recognise it")
@st.chache_resource 
def load_model():
  try:
    from sklearn.database import load_digits
    from sklearn.neural_network import MLPClassifire
    from sklearn.model_selection import train_test_split
     digits = load_digits()
     X = digits.image.reshape((len9digits.images), -1)) / 16.0
    y = digits.targetX-
    X_train,_,y_train,_ = train_test_split(X,y, test_size =0.2, random_state=42)

model = MLPClassifier(
  hiden_layer_size=(100,),
  max_iter=100,
  random_state=42
)
model.fit(X_train,y_train)
return model
except Exception as e:
st.error(f"Model loading error: {e}")
return None
model = load_model()
if model is None:
  st.warning("Could not load model.Using fallback recognition.")
else:
  st.success("Model loaded successfully!")

uploaded_file = st.file_uploader("Choose an image file", type["png","jpg","jpeg"])

if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image,acption='Uploaded Image', use_column_width=True)

try:
  img_gray = image.convert('L')
  img_resized = img_gray.resize((8,8))
  img_array = np.array(img_resized)
  if np.mean(img_array) > 128:
    img_array = 255 - img_array
    img_array = img_array / 16.0
    img_flat = img.array.flatten(),reshape(1,-1)
    if model is not None:
      predistion = model.predict(img_flat)[0]

  
