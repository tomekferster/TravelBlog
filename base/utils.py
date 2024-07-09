import cv2

def crop_image(path):

    # Read the input image 
    img = cv2.imread(path) 

    # Convert into grayscale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    # Load the cascade 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml') 
    
    # Detect faces 
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) 
    
    print(faces)
    padding = 25
    if len(faces) > 1:
        print('Many faces on the picture!')

        # Draw rectangle around the faces and crop the faces 
        # for (x, y, w, h) in faces:
        #     padding = 70
        #     cv2.rectangle(img, (x - padding, y - padding), (x + w + padding, y + h + padding), (0, 0, 255), 0) 
        #     faces = img[y - padding:y + h + padding, x - padding:x + w + padding] 
        #     cv2.imshow("face",faces) 
        #     cv2.imwrite('face.jpg', faces) 
    else:
        try:
            (x, y, w, h) = faces[0]
        except IndexError as e:
            print("Wrong picture! Please upload another!") # should not show during the initial registration!
        else:
            (x, y, w, h) = faces[0]
            cv2.rectangle(img, (x - padding, y - padding), (x + w + padding, y + h + padding), (0, 0, 255), 0)
            face = img[y - padding:y + h + padding, x - padding:x + w + padding]
            cv2.imwrite(path, face) 

    