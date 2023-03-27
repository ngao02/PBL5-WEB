from django.shortcuts import render
import pyrebase
from django.contrib import auth
import firebase_admin
from firebase_admin import credentials

# # Khai báo đường dẫn đến tập tin chứa thông tin xác thực Firebase
# cred = credentials.Certificate('/path/to/serviceAccountKey.json')

# # Khởi tạo ứng dụng Firebase
# firebase_admin.initialize_app(cred)
config = {
    'apiKey': "AIzaSyAq7-ziABaQCTxfeOlMIbv8jvfQk2B7lmQ",
    'authDomain': "pbl5-94125.firebaseapp.com",
    'databaseURL': "https://pbl5-94125-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "pbl5-94125",
    'storageBucket': "pbl5-94125.appspot.com",
    'messagingSenderId': "42461525472",
    'appId': "1:42461525472:web:e0519d8a1a0e0644f1e785",
    'measurementId': "G-K47401613X"
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

def setting(request):
    
    return render(request,"Setting.html")

def postCancel(request):
    return render(request,"MainPage.html") 
    
def postUpdate(request):
    fullName = request.POST.get("fullName")
    eMail=request.POST.get('eMail')
    phone = request.POST.get('phone')
    Adress = request.POST.get('Adress')
    School = request.POST.get('School')
    idtoken = request.session['uid']
    url = request.POST.get('url')
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    data={"fullName":fullName,"eMail":eMail,"phone":phone,"Adress":Adress,"School":School,"url":url}
    database.child("users").child(a).child("profile").set(data)
    
    return render(request,"MainPage.html")  