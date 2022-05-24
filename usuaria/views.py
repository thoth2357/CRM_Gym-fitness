from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    context = {}
    if request.method == 'GET':
        print(request.user)
    return render(request, 'dashboard/dashboard.html', context)

