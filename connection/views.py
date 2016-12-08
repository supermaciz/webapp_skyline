from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from email.utils import format_datetime, localtime


def send_email(contact, msg, obj):
    date = format_datetime(localtime())
    headers = {'Date': date}
    email = EmailMessage(obj, msg, to=[contact], headers=headers)
    try:
        email.send()
    except:
        print("configure email THXKBYE")


def hello(request):
    list_all_users = None
    error = ''
    if request.method == "POST":
        if request.POST.get('login'):
            username = request.POST.get('login')
            passwd = request.POST.get('password')
            user = authenticate(username=username, password=passwd)
            if user:
                login(request, user)
                send_email(user.email, "GOOD", "connection to roger skyline")
        elif request.POST.get('username'):
            username = request.POST.get('username')
            passwd = request.POST.get('password')
            email = request.POST.get('email')
            try:
                user = User(username=username, email=email)
                user.set_password(passwd)
                if request.POST.get("staff"):
                    user.is_staff = True
                user.save()
                send_email(user.email, "registration confirmed", "welcome to roger skyline")
            except:
                error = 'mail or user allready exist'
        elif request.POST.get('user'):
            pk = request.POST.get('user')
            passwd = request.POST.get('password')
            user = User.objects.get(pk=pk)
            if user:
                user.set_password(passwd)
                user.save()
                send_email(user.email, "your new password is: " + passwd, "roger skyline new pass")
        elif request.POST.get('new_password'):
            passwd = request.POST.get('new_password')
            request.user.set_password(passwd)
            request.user.save()
            send_email(request.user.email, "your new password is: " + passwd, "roger skyline new pass")
    elif request.method == "GET":
        if request.GET.get('logout'):
            logout(request)
    if request.user.is_superuser:
        list_all_users = User.objects.all()
    return render(request, 'connection/connection.html',
                  {'list_all_users': list_all_users, 'error': error})
