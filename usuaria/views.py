from django.shortcuts import render

# Create your views here.
def register(request):
    pass

def login(request):
    context = {}
    return render(request, 'Login/index.html', context)

