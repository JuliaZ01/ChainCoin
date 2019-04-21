from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Users,account
from django.contrib.auth import authenticate
import redis
import zerorpc

def login(request):
    if request.method == 'POST':
        ctx = {}
        ctx['msg'] = "Welcome"
        ctx['un'] = request.POST['un']
        ctx['up']= request.POST['up']
        if Users.objects.filter(phone_number = ctx['un']):
            if Users.objects.filter(user_password = ctx['up']):
                request.session['is_login'] = True
                request.session['username'] = ctx['un']
                ctx['msg'] = "欢迎"
            else:
                ctx['msg'] = "密码错误"
        else:
            ctx['msg'] = "用户不存在"
        return render(request,'index/message.html',ctx)

def logout(request):
    request.session.flush()
    return render(request,'index/index.html')

def register(request):
    if request.method == 'POST':
        try:
            U = Users(phone_number = request.POST['phone_number'],user_password = request.POST['user_password'])
        except ValueError:
            return render(request, 'index/message.html', {'msg': "信息未填写或者格式错误"})
        else:
            for Us in Users.objects.all():
                if Us.phone_number == request.POST['phone_number']:
                    return render(request, 'index/message.html', {'msg': "您已经注册过用户"})
            c = zerorpc.Client()
            c.connect("tcp://127.0.0.1:4343")
            kp = c.keypair()
            address = kp[0:36]
            pbkey = kp[36:112]
            prkey = kp[112:]
            # U = Users(phone_number = request.POST['phone_number'],user_password = request.POST['user_password'])
            U = Users(phone_number=request.POST['phone_number'], user_password=request.POST['user_password'],
                      address=address, public_key=pbkey, private_key=prkey)
            U.save()
            A = account(ac_coins=50, ac_users=U)
            A.save()
            try:
                Ut = Users.objects.get(pk=U.id)
                At = account.objects.get(pk=A.id)
            except Users.DoesNotExist:
                return render(request, 'index/message.html', {'msg': "注册失败，请再次尝试"})
            except account.objects.get:
                return render(request, 'index/message.html', {'msg': "注册失败，请再次尝试"})
            else:
                return render(request, 'index/message.html', {'msg': "注册成功"})

    else:
        return render(request, 'login/register.html')

