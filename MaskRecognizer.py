import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import smtplib

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('C:\\Users\\acer\\Pictures\\Saved Pictures\\person 2.jpg')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)

# display the resized image
image.show()

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)
#condition for no mask
if prediction[0][1] > prediction[0][0]:
  # Python code to illustrate Sending mail
  # to multiple users
  # from your Gmail account

  # list of email_id to send the mail 
  li = ["<your email>@gmail.com"] 

  for dest in li: 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("thealphadebuggers@gmail.com", "alphadebuggers12345689") 
    message = "A customer is not wearing a mask!"
    s.sendmail("thealphadebuggers@gmail.com", dest, message) 
    s.quit()
    
#condition for mask
else:
    # Python code to illustrate Sending mail
    # to multiple users
    # from your Gmail account

    # list of email_id to send the mail 
  li = ["<your email>@gmail.com"] 
  for dest in li: 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("thealphadebuggers@gmail.com", "alphadebuggers12345689") 
    message = "A customer is  wearing a mask!"
    s.sendmail("thealphadebuggers@gmail.com", dest, message) 
    s.quit()
