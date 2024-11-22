from django.shortcuts import render

# Create your views here.
def Client(request):
    return render(request, 'Client.html')