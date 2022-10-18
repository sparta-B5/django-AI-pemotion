from django.shortcuts import render, redirect
from .models import Feed

# Create your views here.
def main(request):
    return render(request,'diary/index.html')