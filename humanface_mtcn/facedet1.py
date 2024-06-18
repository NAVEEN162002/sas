import os
import cv2
from mtcnn import MTCNN
import matplotlib.pyplot as plt

def detect_faces(image_path, save_folder):
    # Load the image
    image = cv2.imread(image_path)
    # Convert image to RGB (OpenCV uses BGR by default)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Create an MTCNN detector
    detector = MTCNN()
    
    # Detect faces in the image
    faces = detector.detect_faces(rgb_image)
    
    # Clear the contents of the save folder
    for file in os.listdir(save_folder):
        file_path = os.path.join(save_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    
    # Save each detected face
    for i, face in enumerate(faces):
        x, y, w, h = face['box']
        # Expand the bounding box to increase the border
        expanded_x = max(0, x - 10)
        expanded_y = max(0, y - 10)
        expanded_w = min(image.shape[1], w + 20)
        expanded_h = min(image.shape[0], h + 20)
        # Crop the face region from the image with expanded bounding box
        face_image = image[expanded_y:expanded_y+expanded_h, expanded_x:expanded_x+expanded_w]
        # Save the face image to the save folder
        cv2.imwrite(os.path.join(save_folder, f"face_{i}.jpg"), face_image)

    # Draw border around detected faces in the original image
    for face in faces:
        x, y, w, h = face['box']
        # Expand the bounding box to increase the border
        expanded_x = max(0, x - 10)
        expanded_y = max(0, y - 10)
        expanded_w = min(image.shape[1], w + 20)
        expanded_h = min(image.shape[0], h + 20)
        # Draw rectangle around the expanded face region
        cv2.rectangle(image, (expanded_x, expanded_y), (expanded_x+expanded_w, expanded_y+expanded_h), (255, 0, 0), 2)

    # Return the image with faces and the number of faces detected
    return image, len(faces)

# Path to the image file
image_path = r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\humanface_mtcn\grp5.jpg"
# Folder to save detected faces
save_folder = r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\humanface_mtcn\detected_faces"

# Detect faces, draw borders, and save detected faces
image_with_faces, num_faces = detect_faces(image_path, save_folder)

# Display the image with borders around faces
plt.imshow(cv2.cvtColor(image_with_faces, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
# Print the number of faces detected
print("Total number of faces detected:", num_faces)
