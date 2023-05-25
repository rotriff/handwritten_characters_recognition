import os
import cv2
import numpy as np


from keras.models import load_model

# loading needed model
model = load_model("recognition_model.h5")


# create a dictionary to map the integer values with the characters.
char_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 
             9:'9', 10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',
             18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',
             27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X', 34:'Y',35:'Z'}

# function for values prediction
def predict(image):
    prediction = char_dict[np.argmax(model.predict(image))]
    return prediction


# function for image preparation
def process_image(entry):
    img = cv2.imread(entry)
    # convert the image from BGR to grayscale and apply thresholding to it
    # to keep the image smooth without any hazy gray colors that could lead to wrong predictions.
    img = cv2.GaussianBlur(img, (7, 7), 0)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
    # applying morphological gradient procession for higher prediction accyracy
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))
    img_thresh = cv2.morphologyEx(img_thresh, cv2.MORPH_GRADIENT, element)
    # downscaling
    img_thresh = img_thresh / 255
    # resize into the dimensions that the model takes as input and reshaping the image
    # so that it can be used as model input.
    img_final = cv2.resize(img_thresh, (28, 28))
    img_final = np.reshape(img_final, (1, 28, 28))
    return img_final


#  function for finding needed files and output
def scan(path):
    # Scan the directory and get
    # an iterator of os.DirEntry objects
    # corresponding to entries in it
    # using os.scandir() method
    obj = os.scandir(path)

    # List files in the specified path
    print("Files in '% s':" % path)
    for entry in obj:
        if entry.is_file and entry.name.endswith(
            (
                ".jpg",
                ".jpeg",
                ".png",
            )
        ):
            image = process_image(entry.path)
            prediction = predict(image)
            print(prediction, ",", entry.path)


def main():
    scan(input(r"Enter the path of the folder: "))


if __name__ == "__main__":
    main()
