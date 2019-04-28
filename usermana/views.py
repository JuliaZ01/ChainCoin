from django.http import HttpResponse
from django.shortcuts import render
from .models import Volunteer
from login.models import Users
import zerorpc
from urllib.parse import unquote,quote
def index(request):
    if request.method == 'POST':
        try:
            U = Users.objects.get(phone_number=request.POST['username'])
        except Users.DoesNotExist:
            return render(request, 'usermana/index.html')
        else:
            try:
                volu_list = Volunteer.objects.filter(Vl_user=U)
            except Volunteer.DoesNotExist:
                return render(request, 'usermana/index.html')
            else:
                context = {'volu_list': volu_list}
                return render(request, 'usermana/index.html', context)
    else:
        latest_volu_list = Volunteer.objects.order_by('Vl_name')[:5]
        context = {'volu_list':latest_volu_list}
        return render(request, 'usermana/index.html',context)

def start(request):
    if request.method =='POST':
            try:
                U = Users.objects.get(phone_number=request.session['username'])
            except KeyError:
                return render(request, 'index/message.html', {'msg': "用户未登录，请登录后再进行操作"})
            else:
                try:
                    v = Volunteer(Vl_name = request.POST['name'],Vl_detail = request.POST['detail'],
                                 Vl_user = U)
                except ValueError:
                    return render(request, 'index/message.html', {'msg': "信息未填写或者格式错误"})
                else:
                    users = U.address
                    prkey = U.private_key
                    c = zerorpc.Client()
                    c.connect("tcp://127.0.0.1:4343")
                    hash1 = c.addVolunteer(users, prkey, quote(request.POST['name'], 'utf-8'), quote(request.POST['detail'], 'utf-8'))
                    if type(hash1) == type('abc'):
                        v.save()
                        return render(request, 'index/message.html', {'msg': "您的志愿信息已经提交"})
                    else:
                        return render(request, 'index/message.html', {'msg': "提交失败，请联系管理员。"})
    else:
        return render(request,'usermana/start.html')

def scharge(request):
    return render(request,'usermana/servicecharge.html')