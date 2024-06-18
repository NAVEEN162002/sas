const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/attendance', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = mongoose.connection;

// Define Schema
const studentSchema = new mongoose.Schema({
  s_id: String,
  s_name: String,
  status: {
    type: Array,
    default: [],
  },
});

// Create Model
const Student = mongoose.model('Student', studentSchema);

// Insert Documents
const studentsData = [
  {
    s_id: "20B81A0420",
    s_name: "Hruthik",
  },
  {
    s_id: "20B81A0416",
    s_name: "Dinesh",
  },
  {
    s_id: "20B81A0450",
    s_name: "Srisai",
  },
  {
    s_id: "20B81A0457",
    s_name: "Vignesh",
  },
  {
    s_id: "20B81A0405",
    s_name: "Ashok",
  },
];

// Insert documents with empty status array
db.once('open', async () => {
  try {
    await Student.insertMany(studentsData);
    console.log('Documents inserted successfully.');
  } catch (error) {
    console.error('Error inserting documents:', error);
  } finally {
    mongoose.disconnect();
  }
});
