from django.shortcuts import render

# Create your views here.
def iMain(request):
    return render(request, 'imain.html')

def iCore(request):
    return render(request, 'iCore.html')

def imainHome(request):
    return render(request, 'imainHome.html')

def imainPortfolio(request):
    return render(request, 'imainPortfolio.html')