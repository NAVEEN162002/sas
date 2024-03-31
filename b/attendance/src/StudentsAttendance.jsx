import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Modal component
function Modal({ isOpen, onClose, onConfirm, studentId }) {
  const [password, setPassword] = useState('');

  const handleConfirm = () => {
    if (password === studentId) {
      onConfirm();
      onClose();
    } else {
      alert('Incorrect password');
    }
  };

  return (
    <>
      {isOpen && (
        <div className="fixed inset-0 flex items-center justify-center z-50">
          <div className="modal-overlay bg-black opacity-50 absolute inset-0"></div>
          <div className="modal bg-white p-8 rounded-lg z-10">
            <h2 className="text-xl mb-4">Enter password</h2>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="border border-gray-400 px-4 py-2 rounded-md mb-4"
            />
            <div className="flex justify-center">
              <button
                onClick={handleConfirm}
                className="mr-4 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
              >
                Confirm
              </button>
              <button
                onClick={onClose}
                className="px-4 py-2 bg-gray-300 text-gray-700 rounded-md hover:bg-gray-400"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default function StudentsAttendance() {
  const [students, setStudents] = useState([]);
  const [selectedStudent, setSelectedStudent] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [percentage , setpercentage]= useState(false);

  // Fetch student data from the server when the component mounts
  useEffect(() => {
    axios
      .get('http://localhost:5000/students')
      .then((res) => {
        setStudents(res.data);
      })
      .catch((err) => {
        console.error('Error fetching student data:', err);
      });
  }, []);

  // Function to handle card click
  const handleCardClick = (student) => {
    setSelectedStudent(student);
  };

  // Function to close the modal
  const handleCloseModal = () => {
    setSelectedStudent(null);
  };

  // Function to calculate total percentage attendance
  const calculateAttendance = (statusArray) => {
    if (!statusArray || statusArray.length === 0) return 0;

    const totalDays = statusArray.length;
    const presentDays = statusArray.filter((status) => status === true).length;
    return (presentDays / totalDays) * 100;
  };

  // Function to filter students based on search query
  const filteredStudents = students.filter(
    (student) =>
      student.s_id.includes(searchQuery) ||
      student.s_name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="mt-16">
      <div className='flex justify-center'>
      <h1 className='text-3xl font-bold m-2 text-gray-800'>STUDENTS ATTENDANCE</h1>
      </div>
      <div className="mb-4 flex justify-center">
        <input
          type="text"
          placeholder="Search by ID or name"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="border border-gray-400 px-4 py-2 rounded-md w-full m-5"
        />
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 mt-4">
        {filteredStudents.map((student) => (
          <div
            key={student._id}
            className="bg-white shadow-md rounded-lg cursor-pointer hover:shadow-lg transition duration-300"
            onClick={() => handleCardClick(student)}
          >
            <div className="p-6">
              <p className="text-lg font-semibold mb-2">
                Student ID: {student.s_id}
              </p>
              <p className="text-gray-700">
                <strong>Name:</strong> {student.s_name}
              </p>
            </div>
            <div className="flex justify-center items-center bg-gray-200 py-2">
              <button className="text-blue-500 font-semibold hover:text-blue-700">
                View Attendance
              </button>
            </div>
          </div>
        ))}
      </div>

      {selectedStudent && (
        <Modal
          isOpen={true}
          onClose={handleCloseModal}
          onConfirm={() => {
            const percentageAttendance = calculateAttendance(
              selectedStudent.status
            );
            alert(
              `Total percentage attendance for ${selectedStudent.s_name} (${selectedStudent.s_id}) is ${percentageAttendance.toFixed(
                2
              )}%`
            );
          }}
          studentId={selectedStudent.s_id} // Pass the student's ID to the modal
        />
      )}
    </div>
  );
}