#!C:\Python37\python.exe
import cgi, os, csv
print('content-type:text/html\r\n\r\n')

form = cgi.FieldStorage()
email = str(form.getvalue("email"))
pwd = str(form.getvalue("pwd"))
dogName = str(form.getvalue("dogName"))

file = open('C:\wamp64\www\Doggo\HealthyPooch.csv','r')
data = file.readline()

if email in data:
    print('<html>')
    print('<body style="background-color:#ffffb3"><center>')
    print('<h1>Welcome Back!</h1>')
    print('<img src="dogWave.jpg" style="width:800px; height:60%;">')
    print('<br><br><a href="exercise.html"><button style="width=100px;height:40px;background-color:pink; border: solid 2px white;"> Continue </button></a>')
    print("</center></body></html>")
else:
    print('<html><body style="background-color:#ffcccc;"><center><h1> Unfortunately we were not able to find your account </h1>')
    print('<img src="sadDog.jpeg" style="width:700px;height:80%;"</center>')
    print('<br><br><a href=Signup.html><button style="width:200px; height:50px; background-color:#d580ff; text-color:white; border: solid 3px white;"> Sign up now! </button> </a>')
    print("</body></html>")
