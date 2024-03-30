// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Nav from './Nav';
import Footer from './Footer';
import Home from './Home';
import StudentsAttendance from './StudentsAttendance';
import FacultyLogin from './FacultyLogin';
import ContactUs from './ContactUs';
import StudentsData from './StudentsData';

function App() {
  return (
    <Router>
      <div>
        <Nav />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/students-attendance" element={<StudentsAttendance />} />
          <Route path="/faculty-login" element={<FacultyLogin />} />
          <Route path="/contact-us" element={<ContactUs />} />
          <Route path="/students-data" element={<StudentsData />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
