from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def send_email(contact, msg, obj):
    email = EmailMessage(obj, msg, to=[contact])
    try:
        email.send()
        email.send()
    except:
        print("configure email THXKBYE")


def hello(request):
    list_all_users = None
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
                user = User(username=username, password=passwd, email=email)
                if request.POST.get("staff"):
                    user.is_staff = True
                user.save()
                send_email(user.email, "registration confirmed", "welcome to roger skyline")
            except:
                pass
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
                  {'list_all_users': list_all_users})
