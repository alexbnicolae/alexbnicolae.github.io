var fs = require('fs');
const express = require('express');
var app = express();

app.use('/save',express.static('html'));
app.use('/save',express.urlencoded({extended:true}));

app.get( '/', function(req,res){ res.sendFile('/', {root: __dirname})}); 
app.get( '/index.html', function(req,res){ res.sendFile('/index.html', {root: __dirname})}); 
app.get( '/HTML/Gallery.html', function(req,res){ res.sendFile('/HTML/Gallery.html', {root: __dirname})}); 
app.get( '/HTML/JS.html', function(req,res){ res.sendFile('/HTML/JS.html', {root: __dirname})}); 
app.get( '/HTML/Stats.html', function(req,res){ res.sendFile('/HTML/Stats.html', {root: __dirname})}); 
app.get( '/HTML/Support.html', function(req,res){ res.sendFile('/HTML/Support.html', {root: __dirname})}); 
app.get( '/HTML/date.txt', function(req,res){ res.sendFile('/HTML/date.txt', {root: __dirname})}); 

app.use('/CSS',express.static('CSS'));
app.use('/Imagini',express.static('Imagini'));
app.use('/JS',express.static('JS'));
app.use('/itc-novarese-std-ultra.otf',express.static('itc-novarese-std-ultra.otf'));


app.post('/save',function(request,response){

    response.status = 200;
    response.write("<html><body><p> " + request.body.name + " is "
   + request.body.age + " year(s) old from " + request.body.city + ".</p> </body></html>");
    response.end();
    if (fs.existsSync("Supportes.json"))
   {
       var date= fs.readFileSync("Supportes.json");
       ob=JSON.parse(date);
   }
   else
   ob=[];
   ob.push(request.body);
   fs.writeFileSync("Supporters.json",JSON.stringify(ob));
   });

app.get('/show', function(request,response){
    fs.readFile("supports.json",function(err,date){
    if(err) throw err;
    var supports=JSON.parse(date);
    response.status(200);
   response.write('<html><body><table><tr><td>Supporter</td><td>Age</td><td>City</td></tr>');
   for(s of supports) {
   response.write('<tr><td>');
   response.write(s.name);
   response.write('</td><td>');
   response.write(s.age);
   response.write('</td><td>');
   response.write(s.city);
   response.write('</td></tr>');
   }
   response.write('</table></body></html>');
   response.end();
    });
});
   

app.listen(5000);