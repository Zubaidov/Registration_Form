from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request, 'register/index.html')


def moveto(request):
    f_name = request.GET['cl_fname']
    l_name = request.GET['cl_lname']
    e_email = request.GET['cl_email']
    n_pass = request.GET['cl_pass']
    c_pass = request.GET['cl_cpass']
    r_url = 'https://www.instagram.com/zubaydov.sh/'
    if n_pass == c_pass:
        return HttpResponseRedirect(r_url)
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/')
