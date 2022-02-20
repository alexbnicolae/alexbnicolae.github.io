// server/index.js

const express = require("express");
const app = express();

const PORT = process.env.PORT || 3001;
const request = require('request');

app.use(express.json())

// CORS policy
app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Authorization");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS");
    next();
})

// De aici luam datele din get_brands
app.get("/brands", (req, res) => {
    const options = {
        url: 'https://app.socialinsider.io/api',
        json:true,
        headers: {'content-type' : 'application/json',
        'authorization': 'Bearer API_KEY_TEST'},
        body:    {
            "jsonrpc": "2.0", 
            "id": 0,
            "method": "socialinsider_api.get_brands", 
            "params": {
                "projectname": "API_test"
            }
        }
    }

    request.post(options, (err, postRes, body)=> {
        if (err) {
            return console.log(err);
        }
        res.json(body);
    }) 
});

// De aici luam datele din get_profile_data
app.get("/profile_data/:id.:profile_type.:date_start.:date_end", (req, res) => {
    const options = {
        url: 'https://app.socialinsider.io/api',
        json:true,
        headers: {'content-type' : 'application/json',
        'authorization': 'Bearer API_KEY_TEST'},
        body:    {
            "id" : 1,
            "method" : "socialinsider_api.get_profile_data",
            "params":{
                "id":req.params.id,
                "profile_type": req.params.profile_type,
                "date": {
                    "start": req.params.date_start,
                    "end": req.params.date_end,
                    "timezone": "Europe/London"
                }
            }
        }
    
    }

    request.post(options, (err, postRes, body)=> {
        if (err) {
            return console.log(err);
        }
        res.json(body);
    }) 
});


app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});