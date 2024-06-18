from twilio.rest import Client
import datetime
import json

# Function to read attendance data from the JSON file
def read_attendance_data(file_path):
    with open(file_path, 'r') as file:
        attendance_data = json.load(file)
    return attendance_data

# Function to send attendance status via SMS to each phone number
def send_attendance_status(attendance_data):
    # Twilio credentials
    account_sid = 'ACbcd261952ac9f22bbe8ad2fa6510a441'
    auth_token = 'd9c284b23bbd6bf45aa05b8e0abe6f70'
    twilio_phone_number = '+12722362316'  # Twilio phone number

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Compose message with attendance status, timestamp, and additional message
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    additional_message = "***Msg from Smart Attendance Monitoring System***\n"
    
    for roll_no, info in attendance_data.items():
        status = info["status"]
        message_body = f"Roll Number: {roll_no}\nAttendance Status: {status}\nTimestamp: {timestamp}\n{additional_message}"

        # Send the message to the phone number associated with the roll number
        phone_number = info["phone_number"]
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=phone_number
        )
        print(f"Message sent to {phone_number}. Message SID: {message.sid}")

# Main function
def main():
    # Path to the attendance JSON file
    attendance_json_path = r'attendance_with_phone.json'

    # Read attendance data from file
    attendance_data = read_attendance_data(attendance_json_path)

    # Send attendance status to each phone number
    send_attendance_status(attendance_data)

if __name__ == "__main__":
    main()
