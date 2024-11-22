from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def iLogin(request):
    return render(request, 'iLogin.html')

def iRegister(request):
    return render(request, 'iForm.html')