from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

# Create your views here.

#회원가입
def signup(request) :
    # 요청방식이 GET(값을읽어올때)이면 html로
    if request.method == 'GET' :
        return render(request,'user/signup.html') 
    # 요청방식이 POST(값을주거나/수정/삭제)이면 회원가입으로
    elif request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username=username, password=password, name=name)
            return HttpResponse("회원가입 완료!")
        else:
            return HttpResponse("비밀번호 확인 틀렸습니다")
            
       
    