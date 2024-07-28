// src/index.js
const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('../utils/database');
const authRoutes = require('./routes/authRoutes');

dotenv.config();

const app = express();
connectDB();

app.use(express.json());

app.use('/api/auth', authRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});


