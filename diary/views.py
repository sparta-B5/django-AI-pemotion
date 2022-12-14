from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Diary
from django.contrib import messages
from .ml import mainFunc

# Create your views here.
def main(request):
    user = request.user.is_authenticated
    if user:
        all_diary = Diary.objects.filter(user =request.user).order_by("-created_at")
        context={
            "all_diary":all_diary
        }
        return render(request,'diary/index.html', context)
    else:
        return render(request, 'user/sign-in.html')

def diary_detail(request,id):
    user = request.user.is_authenticated
    if user:
        target_diary= Diary.objects.get(id=id)
        if request.user == target_diary.user:
            #조건이 true - 상세페이지를 띄운다. 
            target={
                'diary':target_diary
            }
            return render(request, 'diary/diary.html', target)
        else:
            messages.add_message(request,messages.ERROR,'해당 게시물작성자로 로그인해주세요.')
            return redirect('/')
    else:
        return redirect('/')


def diary_create(request):
    #게시글 작성하기
    if request.method == 'GET':
        return redirect ('/')

    elif request.method == 'POST':

        new_diary = Diary()
        new_diary.content = request.POST.get('my-content')
        new_diary.user = request.user

        #이미지 업로드
        try:
          new_diary.image = request.FILES['image']
        except:
          new_diary.image = None
        new_diary.save()
        messages.add_message(request,messages.SUCCESS,'게시글이 작성되었습니다.')

        # 직전 감정일지의 이미지로 머신러닝로드 
        last_diary = Diary.objects.last()
        if last_diary.image:
          result = mainFunc(last_diary.image.url)    
          last_diary.emotion_predict, last_diary.emotion_label, last_diary.emotion_percent = list(result.values())
          last_diary.save()
        # 게시글 작성후 작성한 게시글 상세페이지로 이동
        return redirect (f'/diary/{last_diary.id}')

def diary_update(request, id):
    diary = Diary.objects.get(id=id)
    if request.method == 'GET':
        context={
            'diary':diary
        }
        return render(request,'diary/diaryupdate.html', context)

    elif request.method == 'POST':
        if diary.user == request.user:
            
          diary.content = request.POST.get('my-content')

          # 저장여부 판별 : 이전에 저장한 이미지 주소
          prev_image_url = ""
          if(diary.image):
            prev_image_url = diary.image.url

          try:
            diary.image = request.FILES['image']
          except:
            pass
          diary.save()

          # edit_diary = Diary.objects.get(id=id)
          if(diary.image):
            new_image_url = diary.image.url
            print(f"prev_image_url: {prev_image_url},new_image_url: {new_image_url}")
            if prev_image_url!=new_image_url:
              result = mainFunc(diary.image.url)    
              diary.emotion_predict, diary.emotion_label, diary.emotion_percent = list(result.values())
              diary.save()  

          return redirect(f'/diary/{id}')
        else:
            messages.add_message(request,messages.ERROR,'해당 게시물작성자로 로그인해주십시오.')
            return redirect('/')

def diary_delete(request, id):
    user = request.user.is_authenticated
    if user:
        delete_diary = Diary.objects.get(id=id)
        if request.user == delete_diary.user:
            delete_diary.delete()
            return redirect('/')
        else:
            messages.add_message(request,messages.ERROR,'해당 게시물작성자로 로그인해주세요.')
            return redirect('/')

    return redirect('/')

