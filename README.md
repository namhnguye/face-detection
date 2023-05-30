# Face Detection

Draws a rectangle around detected faces from a camera.

I used python and the OpenCV library.

You will need to **pip install opencv-python** in order to **import cv2**.
\
Then you can **python main.py** in the terminal to start the program.
\
Pressing **q** will stop the program. 
\
Make sure you have a camera for your computer.
\
If there are errors finding the path to the .xml file, you may need to change this:
classifier = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")  to 
classifier = cv2.CascadeClassifier("the actual path to this file in your computer in the cv2 library, not this directory") 

The resources that helped me were:
* [The OpenCV class list](https://docs.opencv.org/4.7.0/annotated.html)
* [GeeksforGeeks](https://www.geeksforgeeks.org/opencv-python-tutorial/)
* [Stack Overflow](https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters)

