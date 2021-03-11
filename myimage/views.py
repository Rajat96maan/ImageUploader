from django.shortcuts import render, HttpResponse
from .forms import ImageForm
from .models import Image
from django.views.generic.edit import DeleteView
# Create your views here.

def home(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 return render(request, 'myimage/home.html', {'img':img, 'form':form})

