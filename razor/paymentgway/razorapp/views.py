from django.http import HttpResponse
from django.shortcuts import render
import razorpay
from .models import Payee

# Create your views here.

razor = razorpay.Client(auth=('id', 'key'))


def login(request):
    if 'uname' not in request.COOKIES:
        return render(request, 'login.html', context={'stat_log': 0})
    else:
        return render(request, 'index.html', context={'stat_log': 1, 'uname': request.COOKIES['uname']})


def logged_in(request):
    if 'uname' in request.COOKIES:
        return render(request, 'index.html', context={'uname': request.COOKIES['uname'], 'stat_log': 1})
    elif request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        print 'request', request.POST
        if Payee.objects.filter(name=uname, password=password).exists():
            response = render(request, 'index.html', context={'uname': uname, 'stat_log': 1})
            response.set_cookie(key='uname', value=uname)
            return response

        else:
            return render(request, 'login.html', context={'stat_log': 2})
    else:
        return render(request, 'login.html', context={'stat_log': 0})


def index(request):
    if 'uname' not in request.COOKIES:
        return render(request, 'index.html', context={'stat_log': 0})
    else:
        return render(request, 'index.html', context={'stat_log': 1, 'uname': request.COOKIES['uname']})


def success(request):
    print request.POST
    if request.POST:
        return render(request, 'success.html', context=None)
    else:
        return HttpResponse("Try later")


def logout(request):
    response = render(request, 'index.html', context={'stat_log': 0})
    response.delete_cookie(key='uname')
    return response


