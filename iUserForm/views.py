from django.shortcuts import render

# Create your views here.
def iForm(request):
    return render(request, 'ipanel.html')

def iFormNav(request):
    return render(request, 'iFormNav.html')

def iCoreForm(request):
    return render(request, 'iCoreForm.html')

def imainForm(request):
    return render(request, 'imainForm.html')

def imainPortfolioForm(request):
    return render(request, 'imainPortfolioForm.html')