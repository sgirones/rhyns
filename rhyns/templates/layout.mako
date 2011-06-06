# -*- coding: utf-8 -*- 
<!DOCTYPE html>  
<head>
	
  <meta charset="utf-8">
  <title>Thunderdome</title>
  <meta name="author" content="Pylons Project">
  <link rel="shortcut icon" href="/static/favicon.ico">
  <link rel="stylesheet" href="/static/style.css">

</head>

<style type="text/css">

body, td
{
font-size: 14px;
font-family: arial,verdana,sans-serif;
line-height: 16px;
text-decoration: none;
font-weight: normal;
background-color:#AABAA9;

}

a{color:#4E0008;text-decoration:none;}
a:hover{color:#ED6113;text-decoration:underline;}

.square
{
width:250px;
background-color:#8CB88A;
padding: 5px 10px 5px 10px;
border: 2px solid #046000;
margin: 2px;
}

.square2
{
width:180px;
background-color:#99CCFF;
padding: 5px 10px 5px 10px;
border: 2px solid #3E95EC;
}

.make_float
{
float:left;
}

</style>


<body>


  <div id="page">
    
    ${next.body()}

  </div>


   
</body>
</html>
