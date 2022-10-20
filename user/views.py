from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import logout as auth_logout


# Create your views here.

#회원가입
def sign_up(request) :
    # 요청방식이 GET(값을읽어올때)이면 html로
    if request.method == 'GET' :
        return render(request,'user/sign-up.html') 
    # 요청방식이 POST(값을주거나/수정/삭제)이면 회원가입으로
    elif request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username=username, password=password, name=name) 
            return render(request,'user/sign-in.html')
        else:
            return HttpResponse("비밀번호 확인 틀렸습니다")
            
       
#로그인

def sign_in(request):
    if request.method == "GET":
     return render(request, 'user/sign-in.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        me = User.objects.get(username=username)  # 사용자 불러오기
         
        if me.password == password:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            request.session['user'] = me.username  # 세션에 사용자 이름 저장
        return  render(request, 'base.html')  
    else: 
        return render(request, 'user/sign-in.html')  
    
    
    
#로그아웃
def sign_out(request):
    auth_logout(request)
    #로그아웃되면 다시 로그인 화면으로
    return render(request, 'user/sign-in.html')
   
         
        
