from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Diary
from django.contrib import messages
from .ml import mainFunc

# Create your views here.
def main(request):
    #메인
    # user = request.user.is_authenticated
    # if user:
    all_diary = Diary.objects.all().order_by('-created_at')
    context={
        "all_diary":all_diary
    }
    return render(request,'diary/index.html', context)
    # else:
    # return render(request, 'diary/index.html')

def diary_detail(request,id):
    #게시글 상세페이지
    target_diary= Diary.objects.get(id=id) #왼쪽id DB에 있는 id, 오른쪽이 가져온거
    target={
        'diary':target_diary
    }
    return render(request, 'diary/diary.html', target)

def diary_create(request):
    #게시글 작성하기
    if request.method == 'GET':
        return redirect ('/')

    elif request.method == 'POST':
        # my_user= request.user
        new_diary = Diary()
        # new_diary.user = my_user
        new_diary.content = request.POST.get('my-content')
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
        diary.content = request.POST.get('my-content')
        diary.save()
        
        return redirect(f'/diary/{id}')

def diary_delete(request, id):
    diary = Diary.objects.get(id=id)
    diary.delete()

    return redirect('/')

