from django.http import HttpResponse,Http404
from .models import projects
from login.models import Users
from usermana.models import Blacklist
from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from datetime import datetime,timedelta
from django.utils import timezone
from decimal import *
import redis
import zerorpc

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
@register_job(scheduler, 'cron', hour='23', minute='59',id='task_time')
def job():
    for p in projects.objects.all():
        if p.pjts_now == True :
            timenow = timezone.now()
            if timenow - p.pjts_time > timedelta(days=90):
                p.pjts_now = False
                p.save()
register_events(scheduler)
scheduler.start()

scheduler2 = BackgroundScheduler()
scheduler2.add_jobstore(DjangoJobStore(), "default")
@register_job(scheduler2, 'interval', seconds=60, id='task_time2')
def job2():
    for p in projects.objects.all():
        if p.pjts_bool == False:
            c = zerorpc.Client()
            c.connect("tcp://127.0.0.1:4343")
            result = c.getcontractad(p.pjts_hash)
            if result != []:
                p.pjts_address = result[0]['contract_address']
                p.pjts_bool = True
                p.save()
register_events(scheduler2)
scheduler2.start()

def start(request):
    if request.method =='POST':
            try:
                U = Users.objects.get(phone_number=request.session['username'])
            except KeyError:
                return render(request, 'index/message.html', {'msg': "用户未登录，请登录后再进行操作"})
            else:
                if Blacklist.objects.filter(Bl_user=U):
                    return render(request, 'index/message.html', {'msg': "您在黑名单中，禁止发起项目"})
                try:
                    p = projects(pjts_name = request.POST['name'],pjts_detail = request.POST['detail'],
                                 pjts_coins = Decimal(int(request.POST['coins'])),pjts_users = U)
                except ValueError:
                    return render(request, 'index/message.html', {'msg': "信息未填写或者格式错误"})
                else:
                    users = U.address
                    prkey = U.private_key
                    c = zerorpc.Client()
                    c.connect("tcp://127.0.0.1:4343")
                    hash1 = c.createproject(users, int(request.POST['coins']), prkey)
                    if type(hash1) == type('abc'):
                        p = projects(pjts_name=request.POST['name'], pjts_detail=request.POST['detail'],
                                 pjts_coins=int(request.POST['coins']), pjts_users=U, pjts_hash=hash1,
                                 pjts_address='false')
                        p.save()
                        return render(request, 'index/message.html', {'msg': "已经提交，请稍候在个人账户界面查看项目是否生效"})
                    else:
                        return render(request, 'index/message.html', {'msg': "提交失败，请联系管理员。"})
    else:
        return render(request,'projects/start.html')


def show(request):
    latest_projects_list = projects.objects.order_by('pjts_time')
    context = {'latest_projects_list':latest_projects_list}
    return render(request,'projects/show.html',context)

def detail(request,projects_id):
    try:
        p = projects.objects.get(pk=projects_id)
    except projects.DoesNotExist:
        raise Http404("此项目不存在")
    return render(request, 'projects/detail.html', {'projects': p})
