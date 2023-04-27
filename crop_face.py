import cv2


def crop_face(image_path, output_path, padding=10):
    # Read the input image
    img = cv2.imread(image_path)

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:

        # Add padding around the face crop
        x -= padding
        y -= padding
        w += padding * 2
        h += padding * 2

        # Make sure the coordinates are within the image boundaries
        x = max(0, x)
        y = max(0, y)
        w = min(w, img.shape[1] - x)
        h = min(h, img.shape[0] - y)

        # Crop the image
        face = img[y:y + h, x:x + w]

        # Draw a rectangle around the face
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 80)

        # Save the cropped face image
        cv2.imwrite(output_path, face)
        # Print the coordinates of the cropped face image
        print(f"Cropped face image coordinates: x={x}, y={y}, w={w}, h={h}")
        print(f"Copy image coordinates: {x}, {y}, {w}, {h}")


crop_face('source/black.png', 'face.jpg', 150)
