// services/backendService.js

import axios from 'axios';

const backendUrl = 'https://sas-server-5e8c.onrender.com'; // Replace with your backend server URL

export const fetchDataFromBackend = () => {
  return axios.get(`${backendUrl}/api/data`);
};
