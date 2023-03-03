import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
st.header("Real time classification")
def load_model(path):
    return tf.keras.models.load_model(path)
def predict_prob_and_class(model, img):
    probs = model.predict(tf.expand_dims(img, axis=0))
    max_prob = probs.max()
    preds = probs.argmax()
    class_names = ['Cloudy', 'Rain', 'Shine', 'Sunrise']
    pred_class = class_names[preds]
    return max_prob, pred_class
def load_and_prep_image(filename, img_shape=224, scale=False):
  """
  Reads in an image from filename, turns it into a tensor and reshapes into
  (224, 224, 3).

  Parameters
  ----------
  filename (str): string filename of target image
  img_shape (int): size to resize target image to, default 224
  scale (bool): whether to scale pixel values to range(0, 1), default True
  """
  # Read in the image
#   file = filename.read()
#   img = tf.io.read_file(file)
#   tf.io.decode_raw(
#     filename, 'float')
  # Decode it into a tensor
#   img = tf.io.decode_image(filename)
  # Resize the image
  image = Image.open(filename)
  st.image(image)
  img = np.array(image)
  img = tf.image.resize(img, [img_shape, img_shape])
  if scale:
    # Rescale the image (get all values between 0 and 1)
    return img/255.
  else:
    return img
uploaded_file = st.file_uploader("Upload an image")
if uploaded_file is not None:
   loaded_model = load_model('my_model.h5')
   img = load_and_prep_image(uploaded_file)
   prob, class_name = predict_prob_and_class(loaded_model, img)
   st.write("Class:",class_name)
   st.write("Max_prob",prob)
else:
   st.write("Upload a file")
# url = st.text_input("Enter an url of a Picture")
# if url:
#   img = st.image(url, output_format ='JPEG')
#   loaded_model = load_model('my_model.h5')
#   img = load_and_prep_image(uploaded_file)
#   prob, class_name = predict_prob_and_class(loaded_model, img)
#   st.write("Class:",class_name)
#   st.write("Max_prob",prob)