from django.http import HttpResponse
from django.shortcuts import render
import razorpay
from .models import Payee

# Create your views here.

razor = razorpay.Client(auth=('id', 'key'))


def login(request):
    return render(request, 'login.html', context=None)


def logged_in(request):
    if request.method == 'POST':
        print 'request', request.POST
        if Payee.objects.filter(name=request.POST['uname'], password=request.POST['password']).exists():

            return render(request, 'index.html', context={'uname': request.POST['uname'], 'stat_log': 1})
        else:
            return render(request, 'login.html', context={'stat_log': 0})
    else:
        return render(request, 'login.html', context={'stat_log': 0})


def index(request):

    return render(request, 'index.html', context={})


def success(request):
    print request.POST
    if request.POST:
        return render(request, 'success.html', context=None)
    else:
        return HttpResponse("Try later")




