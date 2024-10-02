require("dotenv").config();
const path = require("path");
const express = require("express");
const mysql = require('mysql');
const cors = require('cors');
const axios = require('axios');
const bodyParser = require('body-parser');
const app = express();

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const _dirname = path.dirname("");
const buildPath = path.join(_dirname, "/build");
app.use(express.static(buildPath));

app.get("/*", function(req, res) {
    res.sendFile(
        path.join(_dirname, "/build/index.html"),
        function(err) {
            if (err) {
                res.status(500).send(err);
            }
        }
    );
});

// Set the backend URL using environment variables
const FLASK_BACKEND_URL = process.env.FLASK_BACKEND_URL || 'http://flask-backend-service:5000';

// Updated /signup route
app.post('/signup', async (req, res) => {
    try {
        const apiUrl = `${FLASK_BACKEND_URL}/api/v1/form/signUP`;  // Use the environment variable
        const { email, name, password } = req.body;

        const postData = { email, name, password };
        const response = await axios.post(apiUrl, postData, {
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.data.message === 'Data inserted successfully!') {
            return res.json({ message: 'Success' });
        } else {
            console.log('Error Inserting the data');
            return res.json({ message: 'Error Inserting the data' });
        }
    } catch (error) {
        console.error('Error:', error);
        return res.json({ message: 'Internal server error' });
    }
});

// Updated /home route
app.post('/home', async (req, res) => {
    try {
        const apiUrl = `${FLASK_BACKEND_URL}/api/v1/form/comment`;  // Use the environment variable
        const { author, comment } = req.body;

        const postData = { author, comment };
        const response = await axios.post(apiUrl, postData, {
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.data === 'Comment inserted successfully') {
            return res.json({ message: 'Success' });
        } else {
            console.log('Error Inserting the data');
            return res.json({ message: 'Error Inserting the data' });
        }
    } catch (error) {
        console.error('Error:', error);
        return res.json({ message: 'Internal server error' });
    }
});

// Updated /login route
app.post('/login', async (req, res) => {
    try {
        const apiUrl = `${FLASK_BACKEND_URL}/api/v1/form/login`;  // Use the environment variable
        const { email, password } = req.body;

        const postData = { email, password };
        const response = await axios.post(apiUrl, postData, {
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.data === 'Login successful') {
            console.log('Login success');
            return res.json({ message: 'Success' });
        } else {
            console.log('Authentication failed');
            return res.json({ message: 'Authentication failed' });
        }
    } catch (error) {
        console.error('Error:', error);
        return res.json({ message: 'Internal server error' });
    }
});

// Set the port
const PORT = process.env.PORT || 8081;
app.listen(PORT, () => {
    console.log("Listening on port", PORT);
});
