import React from 'react';

export default function ContactUs() {
  return (
    <div className="mt-16 p-1 text-white py-12 px-4 sm:px-6 lg:px-8  bg-slate-300">
      <div className="max-w-7xl mx-auto text-black">
        <h2 className="text-3xl font-semibold mb-4">Contact Us</h2>
        <p className="text-lg mb-6">
          We'd love to hear from you! Reach out to us with any questions, comments, or feedback.
        </p>
        <form>
          <div className="mb-4">
            <label htmlFor="name" className="block text-lg mb-2">Your Name</label>
            <input type="text" id="name" name="name" className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 text-black" />
          </div>
          <div className="mb-4">
            <label htmlFor="email" className="block text-lg mb-2">Your Email</label>
            <input type="email" id="email" name="email" className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 text-black" />
          </div>
          <div className="mb-4">
            <label htmlFor="message" className="block text-lg mb-2">Message</label>
            <textarea id="message" name="message" rows="4" className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 text-black"></textarea>
          </div>
          <button type="submit" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-md focus:outline-none focus:shadow-outline">Submit</button>
        </form>
      </div>
    </div>
  );
}
