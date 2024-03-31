import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-4 fixed bottom-0 w-full">
      <div className="container mx-auto flex items-center justify-between px-4">
        <p className="text-sm">&copy; 2024 Your Company. All rights reserved.</p>
        <div className="flex space-x-4">
          <a href="#" className="text-sm hover:text-gray-400">About Us</a>
          <a href="#" className="text-sm hover:text-gray-400">Contact</a>
          <a href="#" className="text-sm hover:text-gray-400">Privacy Policy</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
