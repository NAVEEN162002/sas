import React from 'react';
import { Link } from 'react-router-dom';

function Nav() {
  return (
    <nav className="bg-gray-800 py-4 top-0 fixed w-full">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-white font-bold text-xl ml-5">Attendance Monitoring</div>
        <ul className="flex space-x-10 mr-5">
          <li><Link to="/" className="text-white hover:text-gray-300">Home</Link></li>
          <li><Link to="/students-attendance" className="text-white hover:text-gray-300">Students Attendance</Link></li>
          <li><Link to="/faculty-login" className="text-white hover:text-gray-300">Faculty Login</Link></li>
          <li><Link to="/contact-us" className="text-white hover:text-gray-300">Contact</Link></li>
        </ul>
      </div>
    </nav>
  );
}

export default Nav;
