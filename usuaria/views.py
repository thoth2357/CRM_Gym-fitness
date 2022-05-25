from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.
# @login_required
def dashboard_view(request):
    context = {}
    print(request.user)
    if request.method == 'GET':
        print(request.user)
        if request.user.is_staff == True:
            print('A Staff here')
        else:
            print('non staff here')
    return render(request, 'dashboard/dashboard.html', context)


# def home_view(request):
#     context = {}
#     return redirect()
    