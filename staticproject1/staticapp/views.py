from django.shortcuts import render

# Create your views here.
def img_view(request):
    return render(request,'staticapp/showimage.html')
