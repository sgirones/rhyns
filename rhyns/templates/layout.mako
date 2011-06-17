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
font-color: 16px;
text-decoration: none;
font-weight: normal;
background-color:#cccccc;

}

a{color:#4E0008;text-decoration:none;}
a:hover{color:#ED6113;text-decoration:underline;}

.square
{
width:203px;
background-color:#8CB88A;
padding: 5px 10px 5px 10px;
border: 2px solid #002200;
margin: 2px;
}

.square_gray
{
width:203px;
background-color:#9B9BB;
padding: 5px 10px 5px 10px;
border: 2px solid #002200;
margin: 2px;
}

.square_red
{
width:203px;
background-color:#C69D98;
padding: 5px 10px 5px 10px;
border: 2px solid #002200;
margin: 2px;
}

.square_yellow
{
width:203px;
background-color:#C8C758;
padding: 5px 10px 5px 10px;
border: 2px solid #002200;
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
