import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import backImg from './components/back3.jpg'; // Import the background image

export default function FacultyLogin() {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [showPassword, setShowPassword] = useState(false); // State variable for toggling password visibility

  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Check if username and password match
    if (formData.email === 'faculty' && formData.password === 'faculty') {
      // Navigate to another link if credentials are correct
      navigate('/students-data');
    } else {
      // Handle incorrect credentials here
      alert('Invalid username or password');
    }
  };

  // Function to toggle password visibility
  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div className="bg-cover bg-center min-h-screen" style={{ backgroundImage: `url(${backImg})` }}>
      <div className="flex justify-center items-center min-h-screen">
        <div className='bg-cyan-200 p-8 rounded shadow-lg w-full md:w-1/2 lg:w-1/4'>
          <h2 className='text-2xl font-bold mb-4'>Faculty Login</h2>
          <form onSubmit={handleSubmit}>
            <div className='mb-4'>
              <label className='block text-sm font-medium text-gray-700'>Email Address</label>
              <input
                className='mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
                type='text'
                name='email'
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>
            <div className='mb-4'>
              <label className='block text-sm font-medium text-gray-700'>Password</label>
              <div className='relative'>
                <input
                  className='mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
                  type={showPassword ? 'text' : 'password'} // Toggle between text and password type
                  name='password'
                  value={formData.password}
                  onChange={handleChange}
                  required
                />
                {/* Toggle button */}
                <button
                  type='button'
                  className='absolute inset-y-0 right-0 px-4 py-2'
                  onClick={togglePasswordVisibility}
                >
                  {showPassword ? 'hide' : 'show'}
                </button>
              </div>
            </div>
            <button
              type='submit'
              className='w-full bg-gray-800 hover:bg-gray-950 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline'
            >
              Sign In
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}