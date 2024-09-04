require("dotenv").config();
const path=require("path");
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
const _dirname=path.dirname("");
const buildPath = path.join(_dirname ,"/build");
app.use(express.static (buildPath))
app.get("/*", function(req, res) {
    res.sendFile(
        path.join(_dirname,"/build/index.html "), // Updated path
        function(err) {
            if (err) {
                res.status(500).send(err);
            }
        }
    );
});

app.post('/signup', async (req, res) => {
    try {
        const apiUrl = 'http://127.0.0.1:5000/api/v1/form/signUP';
        const email = req.body.email;
        const name=req.body.name
        const password = req.body.password;

        const postData = {
            email,
            name,
            password
        };
        const response = await axios.post(apiUrl, postData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.data.message==='Data inserted successfully!') {
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
app.post('/home', async (req, res) => {
    try {
        const apiUrl = 'http://127.0.0.1:5000/api/v1/form/comment';
        const author = req.body.author;
        const comment = req.body.comment;
        const postData = {
            author,
            comment
        };
        const response = await axios.post(apiUrl, postData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.data==='Comment inserted successfully') {
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

app.post('/login', async (req, res) => {
    try {
        const apiUrl = 'http://127.0.0.1:5000/api/v1/form/login';
        const email = req.body.email;
        const password = req.body.password;
        const postData = {
            email,
            password
        };
        const response = await axios.post(apiUrl, postData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.data ==='Login successful') {
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

const PORT=process.env.PORT || 8081;
app.listen(process.env.PORT, () => {
    console.log("Listening on port ",process.env.PORT);
});
