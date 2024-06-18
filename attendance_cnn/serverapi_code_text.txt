from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://gubbalamalleswari9:HdkOJsldKisAmAQK@cluster0.xs4mglv.mongodb.net/')
db = client['attendance_db']
attendance_collection = db['attendance']
students_collection = db['students']

@app.route('/attendance', methods=['GET'])
def get_all_attendance():
    attendance_records = list(attendance_collection.find({}, {'_id': 0}))
    return jsonify(attendance_records)

@app.route('/attendance/<roll_no>', methods=['GET'])
def get_attendance_by_roll_no(roll_no):
    attendance_record = attendance_collection.find_one({'roll_no': roll_no}, {'_id': 0})
    return jsonify(attendance_record)

@app.route('/attendance', methods=['POST'])
def create_attendance():
    data = request.get_json()
    attendance_collection.insert_one(data)
    return jsonify({"message": "Attendance record created successfully"})

@app.route('/attendance/<roll_no>', methods=['PUT'])
def update_attendance(roll_no):
    data = request.get_json()
    attendance_collection.update_one({'roll_no': roll_no}, {'$set': data})
    return jsonify({"message": "Attendance record updated successfully"})

@app.route('/attendance/<roll_no>', methods=['DELETE'])
def delete_attendance(roll_no):
    attendance_collection.delete_one({'roll_no': roll_no})
    return jsonify({"message": "Attendance record deleted successfully"})

@app.route('/students', methods=['GET'])
def get_all_students():
    students = list(students_collection.find({}, {'_id': 0}))
    return jsonify(students)

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    students_collection.insert_one(data)
    return jsonify({"message": "Student record created successfully"})

if __name__ == '__main__':
    app.run(debug=True)
