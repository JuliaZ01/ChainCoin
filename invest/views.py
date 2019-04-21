from django.shortcuts import render
from django.http import HttpResponse
from projects.models import projects
from login.models import Users,account
from .models import investbill
import zerorpc
# Create your views here.
global ProjectId
def invest(request,projects_id):
        try:
            p = projects.objects.get(pk=projects_id)
        except projects.DoesNotExist:
            return render(request, 'index/message.html', {'msg': "本项目不存在"})
        else:
            if projects.pjts_now == False:
                return render(request, 'index/message.html', {'msg': "本项目已经截止"})
            else:
                p = projects.objects.get(pk=projects_id)
                U = Users.objects.get(phone_number=request.session['username'])
                if p.pjts_users == U:
                    return render(request, 'index/message.html', {'msg': "不允许跟投自己的项目"})
                else:
                    global ProjectId
                    ProjectId = projects_id
                    return render(request,'invest/invest.html')

def start(request):
    if request.method == 'POST':
        global ProjectId
        projects_id = ProjectId
        try:
            U = Users.objects.get(phone_number=request.session['username'])
        except KeyError:
            return render(request, 'index/message.html', {'msg': "用户未登录，请登录后再进行操作"})
        else:
            coins = int(request.POST['coins'])
            ps = request.POST['ps']
            p = projects.objects.get(pk=projects_id)
            a = account.objects.get(ac_users=U)
            i = investbill(iv_coins=coins, iv_from=U, iv_to=p,iv_ps=ps)
            p.pjts_nowcoins += coins
            if p.pjts_nowcoins > p.pjts_coins:
                 context = {'msg': "您捐赠的金额已经超过项目所需资金"}
            elif coins > a.ac_coins:
                context = {'msg': "余额不足。"}
            elif projects.pjts_now == False:
                context = {'msg': "本项目无效。"}
            elif U.bool == False:
                context = {'msg': "您的用户刚注册，请稍后再投资"}
            else:
                c = zerorpc.Client()
                c.connect("tcp://127.0.0.1:4343")
                info = c.investproject(U.address, U.private_key, p.pjts_address, coins)
                if type(info) != type('abc'):
                    context = {'msg': "捐款失败，请联系管理员。"}
                else:
                    a.ac_coins -= coins
                    p.save()
                    i.save()
                    a.save()
                    context = {'msg': "捐赠成功，感谢您的慷慨"}
        return  render(request,'index/message.html',context)