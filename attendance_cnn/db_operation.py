import json
from pymongo import MongoClient

# Connect to MongoDB Atlas cluster
client = MongoClient("mongodb+srv://gubbalamalleswari9:HdkOJsldKisAmAQK@cluster0.xs4mglv.mongodb.net/")
db = client['attendance']
students_collection = db['student']

def update_status_in_mongodb(json_file_path):
    # Read JSON data from file
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    
    # Extracts a list of all the roll numbers present in the JSON file
    present_roll_numbers = [record['s_id'] for record in json_data]

    # Retrieve all student documents from the MongoDB collection
    all_students = students_collection.find()

    # Iterate through each student document in the collection
    for student_doc in all_students:
        s_id = student_doc['s_id']
        
        # Check if the student's roll number is present in the JSON data
        if s_id in present_roll_numbers:
            # If present, mark the status as true
            student_doc['status'].append(True)
        else:
            # If not present, mark the status as false
            student_doc['status'].append(False)
        
        # Update the student document in the MongoDB collection
        students_collection.update_one({'_id': student_doc['_id']}, {'$set': {'status': student_doc['status']}})

if __name__ == '__main__':
    # Path to JSON file containing status data
    json_file_path = r"C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\attendance-tracker\public\attendance.json"

    # Execute the function with the JSON file path
    update_status_in_mongodb(json_file_path)
