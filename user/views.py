from re import fullmatch
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login


# Create your views here.


#회원가입
def sign_up(request) :
    # 요청방식이 GET(값을읽어올때)이면 html로
    if request.method == 'GET' :
        return render(request,'user/sign-up.html') 
    # 요청방식이 POST(값을주거나/수정/삭제)이면 회원가입으로
    elif request.method == 'POST':
        username = request.POST.get('username','')
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        passwordcheck = request.POST.get('passwordcheck', '')
        
        #정규식
        REGEX_PASSWORD = '^(?=.*[\d])(?=.*[a-zA-Z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,16}$'
        
        if password != passwordcheck: 
            return render(request,'user/sign-up.html',{'error': '패스워드를 확인해 주세요!'})
        elif username == '':
            return render(request,'user/sign-up.html',{'error': '아이디는 필수 입니다!'}) 
        elif password == '':
            return render(request,'user/sign-up.html',{'error': '비밀번호는 필수 입니다!'})
        elif username == '' and password == '':
            return render(request,'user/sign-up.html',{'error': '아이디와 비밀번호는 필수 입니다!'})
        elif not fullmatch(REGEX_PASSWORD, password): 
            return render(request,'user/sign-up.html', {'error': '비밀번호는 8~16자리 영문, 숫자, 특수문자 조합만 가능합니다!'} )
        else:
            User.objects.create_user(username=username, password=password, name=name)
            return redirect('/user/sign-in/')
    

#로그인

def sign_in(request):
    if request.method == "GET":
     return render(request, 'user/sign-in.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if username == '':
            return render(request,'user/sign-in.html', {'error': '아이디를 입력해주세요.'} )
        elif password == '':
            return render(request,'user/sign-in.html', {'error': '비밀번호를 입력해주세요.'} )
        elif user is None:
            return render(request,'user/sign-in.html', {'error': '아이디와 비밀번호 확인 해주세요..'} )
        elif user is not None:
            login(request, user)   
            return redirect('/')
   
    
#로그아웃
def sign_out(request):
    auth_logout(request)
    #로그아웃되면 다시 로그인 화면으로
    return render(request, 'user/sign-in.html')
   
         
        
