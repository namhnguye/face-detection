import cv2

# loads the data/instructions for recognizing a face into memory
classifier = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml") 

# start the camera
camera = cv2.VideoCapture(0) 

while True:
    _, frame = camera.read() # camera.read() returns two values, a bool if the frame was read successfully ( _ in this case since it is not used)
                             # and frame, which is the frame from the camera
                             # an infinite loop is used so the frames keep being returned

    # converting these colored frames into grayscale frames, which makes the image processing simpler
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # returns a list of rectangles with coordinates(x, y) for the top left corner and dimensions(width, height) of the rectangle
    # these rectangles only include detected faces
    faces = classifier.detectMultiScale(grayFrame, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30)) 
    
    # draw a rectangle around each colored frame that has a face with the coordinates and dimensions provided
    # the (x, y) is the top left corner, and (x+width, y+height) is the bottom right corner
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0,0,255), 2)
    
    # open a window and constantly shows and updates the frame(detected face) being shown to a newer one
    cv2.imshow("Face Detection (press 'q' to exit)", frame) 

    # exit when 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

camera.release() # free up the resources used for the camera
cv2.destroyAllWindows() # close the window