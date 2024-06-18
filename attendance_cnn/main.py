import cv2 as cv
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from mtcnn import MTCNN
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet
import json
from datetime import datetime
import subprocess
from openpyxl import Workbook

# Initialize MTCNN detector
detector = MTCNN()

# Run facedet1.py as a subprocess to get the number of faces detected
result = subprocess.run(['python', r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\humanface_mtcn\facedet1.py"], capture_output=True, text=True)
output = result.stdout.strip()
num_faces = int(output.split(":")[-1].strip())
print("Total number of faces detected in facedet1.py:", num_faces)

# Initialize FaceNet
facenet = FaceNet()
faces_embeddings = np.load(r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\attendance_cnn\faces_embeddings_done_4classes.npz")
Y = faces_embeddings['arr_1']
encoder = LabelEncoder()
encoder.fit(Y)
model = pickle.load(open("svm_model_160x160.pkl", 'rb'))

# Specify the directory containing images
images_directory = r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\humanface_mtcn\detected_faces"

# Specify the JSON file path
json_file = r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\attendance-tracker\public\attendance.json"

# Specify the confidence threshold (adjust as needed)
confidence_threshold = 0.9

# Get the current timestamp
timestamp = datetime.now()
timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

# Define a dictionary to map student names to roll numbers
roll_no_mapping = {
    "krishna": "20B81A0453",
    "ravi": "20B81A0440",
    "srinu": "20B81A0455",
    "harshith": "20B81A0419",
    "neela": "20B81A0427",
    "naveen": "20B81A0426",
    "hari": "20B81A0451",
    "srisai": "20B81A0450",
    "vignesh": "20B81A0457",
    "hruthik": "20B81A0420",
    "dinesh": "20B81A0416",
    "ashok": "20B81A0405"
}

# Initialize a list to store attendance data
attendance_data = []

# Process each image in the directory
for image_name in os.listdir(images_directory):
    image_path = os.path.join(images_directory, image_name)

    # Read the image
    frame = cv.imread(image_path)

    # Convert image to RGB for MTCNN
    rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Detect faces using MTCNN
    faces = detector.detect_faces(rgb_img)

    # Process each detected face
    for face in faces:
        x, y, w, h = face['box']
        face_img = rgb_img[y:y+h, x:x+w]  # Crop the face region
        resized_face_img = cv.resize(face_img, (160, 160))  # Resize to 160x160
        resized_face_img = np.expand_dims(resized_face_img, axis=0)  # Add batch dimension
        ypred = facenet.embeddings(resized_face_img)  # Generate embeddings
        face_name = model.predict(ypred)  # Predict using the model
        confidence = model.decision_function(ypred)
        final_name = encoder.inverse_transform(face_name)[0]

        # Check confidence level
        if confidence[0].any() >= confidence_threshold:
            roll_no = roll_no_mapping.get(final_name.lower(), "Unknown")
            print(f"Final Name: {final_name}, Roll No: {roll_no} for image {image_name}")
            attendance_data.append({"s_id": roll_no, "s_name": final_name, "status": "Present"})
        else:
            print(f"Unknown face detected in {image_name}")
            attendance_data.append({"s_id": "Unknown", "s_name": "unknown_face", "status": "Present"})

        # Draw rectangle and text on the face
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
        cv.putText(frame, str(final_name), (x, y-10), cv.FONT_HERSHEY_SIMPLEX,
                   1, (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("Face Recognition:", frame)
    cv.waitKey(0)

cv.destroyAllWindows()

# Save the attendance data to JSON file
with open(json_file, 'w') as outfile:
    json.dump(attendance_data, outfile, indent=4)

# Execute db_operation.py script
subprocess.run(['python', r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\attendance_cnn\db_operation.py"], capture_output=True, text=True)

# Execute mob.py script
subprocess.run(['python', r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\attendance_cnn\mob.py"], capture_output=True, text=True)

# Execute msg.py script
subprocess.run(['python', r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\attendance_cnn\msg.py"], capture_output=True, text=True)