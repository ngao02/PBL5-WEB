from django.shortcuts import render
import pyrebase
from django.contrib import auth
config = {
    'apiKey': "AIzaSyBjMGIGKZWGTNBvnlNIu0yHYAo18PlM73g",
  'authDomain': "pbl-demo-9aa60.firebaseapp.com",
  'databaseURL': "https://pbl-demo-9aa60-default-rtdb.firebaseio.com",
  'projectId': "pbl-demo-9aa60",
  'storageBucket': "pbl-demo-9aa60.appspot.com",
  'messagingSenderId': "819068306714",
  'appId': "1:819068306714:web:69dd60ef897c74603f58a3"
}
firebase = pyrebase.initialize_app(config)
database=firebase.database()
authe = firebase.auth()

def login(request):
    return render(request, "login.html")

def postsign(request):
    email=request.POST.get('email1')
    password = request.POST.get('password1')
    try:
        user = authe.sign_in_with_email_and_password(email,password)
    except:
        message = "invalid cerediantials"
        return render(request,"login.html",{"msg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "MainPage.html")

def logout(request):
    auth.logout(request)
    return render(request,'login.html')

def signUp(request):
    message = "add user"
    return render(request,"login.html",{"msg":message})

def postsignUp(request):
    username = request.POST.get("username")
    email=request.POST.get('email')
    password = request.POST.get('password')
    user = authe.create_user_with_email_and_password(email,password)
    uid= user['localId']
    data={"username":username,"email":email,"password":password}
    database.child("users").child(uid).child("details").set(data)
    
    return render(request,"login.html")
    
    