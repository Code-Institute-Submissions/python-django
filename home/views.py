from django.shortcuts import render

# Create your views here.

#Routing, where you are directing the urls and how they are requesting by my code
def index(request):
    return render(request, 'index.html')




