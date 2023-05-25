import numpy as np
import pandas as pd

from tensorflow import keras
from sklearn.model_selection import train_test_split

# provide dataset csv file here
data = pd.read_csv("eng_char_hand_dataset.csv")

# split data into flattened images X and their labels y
X = data.drop("0", axis=1)
y = data["0"]

# splitting the data into training & testing dataset 
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.2)

# reshaping the train & test data so that they can be displayed as an image if needed
train_x = np.reshape(train_x.values, (train_x.shape[0], 28, 28))
test_x = np.reshape(test_x.values, (test_x.shape[0], 28, 28))

# downsampling the values for higher accuracy
train_x = train_x / 255
test_x = test_x / 255

# creating model
model = keras.Sequential(
    [
        # fitting data into model with flatten level
        keras.layers.Flatten(input_shape=(28, 28)),
        # dense layers
        keras.layers.Dense(144, activation="relu"),
        keras.layers.Dense(72, activation="relu"),
        # output level
        keras.layers.Dense(36, activation="softmax"),
    ]
)

# compiling model, defining optimaze and loss functions
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# fitting trainning data into model and train for 10 epochs
model.fit(train_x, train_y, epochs=10)

# evaluating model on test dataset
print(model.evaluate(test_x, test_y))

# save model into file for further usage
model.save(r"recognition_model.h5")
