from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .forms import *
from .do_recognition import *
from .models import *
import base64
import os
import datetime


@login_required
def home(request):
    subjects = Subject.objects.filter(user=request.user)
    return render(request, 'index.html', locals())


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('home', args=[]))
    else:
        if request.method == 'POST':
            ulf = UserLoginForm(request.POST)
            if ulf.is_valid():
                user = authenticate(
                    username=ulf.cleaned_data['username'],
                    password=ulf.cleaned_data['password'], )
                if user is not None:
                    if user.is_active:
                        # 登陆成功
                        login(request, user)
                        return redirect(reverse('home', args=[]))
                    else:
                        # 账号停用
                        error = "账号停用!"
                else:
                    # 账号密码错误
                    error = "账号或密码错误."
            else:
                # error = ulf.errors
                error = "请输入正确的账号密码."
                print(error)
        return render(request, "login.html", locals())


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
def do_check(request):
    result = []
    if request.method == 'POST':
        salt = "data:image/jpeg;base64,"
        img = request.POST.get("photoinput", None)
        subject = request.POST.get('subject', None).split("-")[0]
        subject = Subject.objects.filter(subject_name=subject)[0]
        if img and subject:
            img = base64.b64decode(img.replace(salt, ""))
            path = os.path.join("unknown_faces", str(subject))
            file = open(path, 'wb')
            file.write(img)
            file.close()

            # do check
            do_check_func(subject, path)

            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            url = reverse('query') + "?year=%s&month=%s&day=%s&subject=%s" % (year, month, day, str(subject))
            return redirect(url)

    else:
        return redirect(reverse('home'))


@login_required
def query(request):
    subjects = Subject.objects.filter(user=request.user)
    year = request.GET.get("year", None)
    month = request.GET.get("month", None)
    day = request.GET.get("day", None)
    if year and month and day:
        try:
            date = "%4d-%02d-%02d" % (int(year), int(month), int(day))
            results = Result.objects.filter(result_datetime__icontains=date)
        except TypeError:
            error = "请输入正确的查询日期"
        except ValueError:
            error = "请输入查询日期"

    return render(request, 'query.html', locals())
