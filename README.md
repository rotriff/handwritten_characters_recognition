# Handwritten characters recognition model
## Info
Model for handwritten character recognition (A-Z and 0-9).
Datased used for training contained handwritten english alphabets 
and numbers images in size 28*28 pixels.Images are stored as Gray-level
Pixel values are in range from 0 to 255 which represents the intensity of each 
pixel in the image and they are normalized to represent value between 0 and 1.
Neural network contains 1 flatten level, 144 node input level, 72 node hidden level
and 36 node output level.

Model loss and accuracy data with train data:
loss: 0.0817 - accuracy: 0.9726

Model loss and accuracy data with test data:
loss: 0.1509 - accuracy: 0.9589

data.info()
class 'pandas.core.frame.DataFrame'
RangeIndex: 275450 entries, 0 to 275449
Columns: 785 entries, 0 to 784
dtypes: int64(785)
memory usage: 1.6 GB

To train model, you should provide dataset. (Initial dataset not included to minimize space usage).

With the real test images model unfortunately 
doesn't show high accuracy, so needs to be improved.

## Usage
Main script is check.py. It takes path to directory with images as input
and prints recognized character and path to image.
Use docker build command from directory that contains /app and /test_data,
then use docker run command and provide path with images to predict values.

EXAMPLE:

docker run -it --rm DOCKER_IMAGE_NAME python3 /app/check.py 

Enter the path of the folder: /test_data

Files in '/test_data':

X , /test_data/X.jpg
1/1 [==============================] - 0s 14ms/step

C , /test_data/C.jpg
1/1 [==============================] - 0s 13ms/step

D , /test_data/D.jpg
1/1 [==============================] - 0s 14ms/step

3 , /test_data/3.png
1/1 [==============================] - 0s 15ms/step

7 , /test_data/1.jpg
1/1 [==============================] - 0s 14ms/step

Y , /test_data/Y.jpg
1/1 [==============================] - 0s 13ms/step

A , /test_data/A1.jpg
1/1 [==============================] - 0s 13ms/step

O , /test_data/O.jpg
1/1 [==============================] - 0s 14ms/step


## Packages used
- [Tensorflow](https://www.tensorflow.org/)
- [Scikit-learn](http://scikit-learn.org)
- [OpenCV](https://opencv.org/)
- [Numpy](http://www.numpy.org/)
- [Pandas](https://pandas.pydata.org/)

### Contacts
talleyranv@gmail.com


Made by Vova Taran

