from django.shortcuts import render, redirect
from .models import Diary
from .ml import mainFunc

# Create your views here.
def main(request):
    return render(request,'diary/index.html')

def img_view(request, id):
    detail_diary = Diary.objects.get(id=id)
    return render(request,'diary/img_view.html',{"diary":detail_diary})

def img_upload(request):
  if request.method=="POST":
    new_diary = Diary()
    try:
        new_diary.image = request.FILES['image']
    except:
        new_diary.image = None
    new_diary.save()

    # 마지막 감정일지의 이미지로 머신러닝로드 
    last_diary = Diary.objects.latest('id')
    result = mainFunc(last_diary.image.url)    
    last_diary.emotion_predict, last_diary.emotion_label, last_diary.emotion_persent = list(result.values())
    last_diary.save()
    return redirect('/img-view/'+str(last_diary.id))
    
  else:
    return render(request,'diary/img_upload.html')

