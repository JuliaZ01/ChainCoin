from django.shortcuts import render
from login.models import Users,account
from invest.models import investbill
from projects.models import projects
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime,timedelta
import redis
import zerorpc
import time
# Create your views here.
def index(request):
        U = Users.objects.get(phone_number = request.session['username'])
        a = account.objects.get(ac_users = U)
        msg = {}
        msg['coins'] = a.ac_coins
        # 我的项目 帮助过我的人 我的捐赠记录
        try:
            p = projects.objects.get(pjts_users = U)
        except projects.DoesNotExist:
            msg['my_project'] = False
            msg['helper_list'] = False
            try:
                i = investbill.objects.filter(iv_from=U)
            except investbill.DoesNotExist:
                msg['bill_list'] = False
                return render(request, 'accounts/index.html', msg)
            else:
                msg['bill_list'] = i
                return render(request, 'accounts/index.html', msg)
        else:
            msg['my_project'] = p
            try:
                helper = investbill.objects.filter(iv_to = p)
            except investbill.DoesNotExist:
                msg['helper_list'] = False
                try:
                    i = investbill.objects.filter(iv_from=U)
                except investbill.DoesNotExist:
                    msg['bill_list'] = False
                    return render(request, 'accounts/index.html', msg)
                else:
                     msg['bill_list'] = i
                     return render(request, 'accounts/index.html', msg)
            else:
                msg['helper_list'] = helper
                try:
                    i = investbill.objects.filter(iv_from=U)
                except investbill.DoesNotExist:
                    msg['bill_list'] = False
                    return render(request, 'accounts/index.html', msg)
                else:
                     msg['bill_list'] = i
                     return render(request, 'accounts/index.html', msg)


def settle(request):
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4343")
    U = Users.objects.get(phone_number = request.session['username'])
    p = projects.objects.get(pjts_users = U)
    a = account.objects.get(ac_users = U)
    msg = {}
    if p.pjts_now == True and p.pjts_nowcoins != p.pjts_coins:
        msg['msg'] = "您的项目未到达截止时间"
    elif p.pjts_nowcoins == p.pjts_coins:
        info = c.settleContract(p.pjts_address)
        msg['msg'] = "恭喜您筹到目标金额,钱已汇入您账上"
        p.pjts_now = False
        a.ac_coins += p.pjts_coins
        p.save()
        a.save()
    elif p.pjts_nowcoins == p.pjts_coins:
        info = c.settleContract(p.pjts_address)
        msg['msg'] = "恭喜您筹到目标金额,钱已汇入您账上"
        p.pjts_now = False
        a.ac_coins += p.pjts_coins
        p.save()
        a.save()
    else:
        info = c.settleContract(p.pjts_address)
        msg['msg'] = "很遗憾，您的项目失败"
        for i in investbill.objects.filter(iv_to=p):
            helper = i.iv_from
            a_helper = account.objects.get(ac_users=helper)
            a_helper.ac_coins += i.iv_coins
            p.pjts_nowcoins -= i.iv_coins
            a_helper.save()
        p.save()
    return render(request, 'index/message.html', msg)
