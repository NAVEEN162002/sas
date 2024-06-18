import json
import os

# Roll number mapping with mobile numbers
roll_no_mapping = {
    "20B81A0453": "+918309389269",
    "20B81A0440": "+918309389269",
    "20B81A0455": "+918309389269",
    "20B81A0419": "+918309389269",
    "20B81A0427": "+918309389269",
    "20B81A0426": "+918309389269",
    "20B81A0451": "+918309389269",
    "20B81A0450": "+918309389269",
    "20B81A0457": "+918309389269",
    "20B81A0420": "+918309389269",
    "20B81A0416": "+918309389269",
    "20B81A0405": "+918309389269"
}

# Path to the attendance JSON file
attendance_json_path = r'C:\Users\Naveen Yavvari\OneDrive\Desktop\MAJOR\attendance-tracker\public\attendance.json'

# Read attendance data from JSON file
with open(attendance_json_path, 'r') as file:
    attendance_data = json.load(file)

# Create a new dictionary to store roll numbers, statuses, and phone numbers
result = {}

# Iterate through each attendance record
for record in attendance_data:
    s_id = record.get('s_id')
    s_name = record.get('s_name')
    status = record.get('status')
    if s_id in roll_no_mapping:
        phone_number = roll_no_mapping[s_id]
        result[s_id] = {"status": status, "phone_number": phone_number}

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Write the result to a new JSON file in the script directory
output_json_path = os.path.join(script_directory, 'attendance_with_phone.json')
with open(output_json_path, 'w') as outfile:
    json.dump(result, outfile, indent=4)

print("JSON file generated successfully at:", output_json_path)
