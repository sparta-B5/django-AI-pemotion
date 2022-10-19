from django.shortcuts import render, redirect
from .models import Diary

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
    return redirect('/img-view/'+str(new_diary.id),{'diary':new_diary})
    
  else:
    return render(request,'diary/img_upload.html')

