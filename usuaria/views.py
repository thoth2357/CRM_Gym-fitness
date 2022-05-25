from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    context = {}
    if request.method == 'GET':
        if request.user.is_staff == True:
            print('A Staff here')
        else:
            pass
    return render(request, 'dashboard/dashboard.html', context)

