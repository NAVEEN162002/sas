import React, { useState, useEffect } from 'react';
import backgroundImage from './components/back2.jpg'; // Import your background image

export default function Home() {
  const [text, setText] = useState('');
  const phrases = [
    'WELCOME TO SMART ATTENDANCE MONITORING SYSTEM',
    'TRACK ATTENDANCE EFFICIENTLY',
    'ENHANCE PRODUCTIVITY',
    // Add more phrases as needed
  ];
  const typingDelay = 50;
  const pauseDelay = 2000; // Pause between phrases

  useEffect(() => {
    let currentIndex = 0;
    let currentText = '';
    let isTyping = true;

    const type = () => {
      const currentPhrase = phrases[currentIndex];

      if (isTyping) {
        currentText = currentPhrase.substring(0, currentText.length + 1);
        setText(currentText);

        if (currentText === currentPhrase) {
          isTyping = false;
          setTimeout(type, pauseDelay);
        } else {
          setTimeout(type, typingDelay);
        }
      } else {
        currentText = currentPhrase.substring(0, currentText.length - 1);
        setText(currentText);

        if (currentText === '') {
          isTyping = true;
          currentIndex = (currentIndex + 1) % phrases.length;
          setTimeout(type, typingDelay);
        } else {
          setTimeout(type, typingDelay);
        }
      }
    };

    type();
  }, []);

  return (
    <div className='h-screen flex flex-col justify-center items-center' style={{ backgroundImage: `url(${backgroundImage})`, backgroundSize: 'cover' }}>
      <div className='text-center text-4xl font-bold uppercase text-black'>
        {text}
      </div>
    </div>
  );
}
