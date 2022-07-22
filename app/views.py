from ast import Param
from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

import random
import datetime
import csv

from dateutil.relativedelta import relativedelta
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from requests import request

from .models import Card
from .forms import  ComentForm, MainForm


#top
@login_required(login_url='/accounts/login/')
def index(request,page=1):
    data=get_data(request.user,  page)
    data2=get_data2(request.user, page)
    params={
        'login_user':request.user,
        'data':data,
        'data2':data2
        
    }
    return render(request,'tarot/index.html',params)


def get_data(owner1, page):
    page_num = 5
    t = datetime.date.today()
    t1 = t + relativedelta(months=-6)
    data = Card.objects.filter(pub_date__gt=t1).filter(owner=owner1)
    page_item = Paginator(data, page_num)
    return page_item.get_page(page)

def get_data2(owner1, page):
    page_num = 5 
    t = datetime.date.today()
    t1 = t + relativedelta(months=-6)
    t2=-1
    data2 = Card.objects.filter(pub_date__lt=t1).filter(owner=owner1).filter(point=-1)
    page_item = Paginator(data2, page_num)
    return page_item.get_page(page)



#過去
@login_required(login_url='/accounts/login/')
def past(request,page=1):
    data3=get_data3(request.user, page)
    params={
        'login_user':request.user,
        'data':data3,
    }
    return render(request,'tarot/past.html',params)

def get_data3(owner1, page):
    page_num = 10 
    data3 = Card.objects.filter().filter(owner=owner1)
    page_item = Paginator(data3, page_num)
    return page_item.get_page(page)

#ポイント処理
@login_required(login_url='/accounts/login/')
def point(request,num):
    data4=Card.objects.get(id=num)
    data4.point =1
    data4.save()
    return redirect(to="/tarot")    

#ポイント処理
@login_required(login_url='/accounts/login/')
def point1(request,num):
    data5=Card.objects.get(id=num)
    data5.point =0
    data5.save()
    return redirect(to="/tarot")     

#占いスタート
@login_required(login_url='/accounts/login/')
def start(request):
    if (request.method == 'POST'):
        cardrand = []
        while len(cardrand) < 13:
            n = random.randint(1, 78)
            if not n in cardrand :
                cardrand .append(n)
        for randj in range(13):
            b = random.randint(0, 1)
            c = [-1, 1]
            cardrand[randj] = int(cardrand[randj] )* c[b]

        tarcard = Card()
        tarcard.owner=request.user
        tarcard.card1=cardrand[0]
        tarcard.card2=cardrand[1]
        tarcard.card3=cardrand[2]
        tarcard.card4=cardrand[3]
        tarcard.card5=cardrand[4]
        tarcard.card6=cardrand[5]
        tarcard.card7=cardrand[6]
        tarcard.card8=cardrand[7]
        tarcard.card9=cardrand[8]
        tarcard.card10=cardrand[9]
        tarcard.card11=cardrand[10]
        tarcard.card12=cardrand[11]
        tarcard.card13=cardrand[12]
        coment = ComentForm(request.POST, instance=tarcard)
        coment.save()
        num=tarcard.id
        html="/tarot/answer/"+str(num)
        return redirect(to=html)    

    params={
        'login_user':request.user,
        'form':ComentForm(),
    }
    return render(request,'tarot/start.html',params)



#表示
@login_required(login_url='/accounts/login/')
def answer(request,num):

    cardname=[]
    with open('./app/card2.csv', encoding="utf_8") as f1:
        reader1 = csv.reader(f1)
        cardname = [row for row in reader1]


    cardmean1=[]
    with open('./app/card.csv', encoding="utf_8") as f:
        reader = csv.reader(f)
        cardmean1 = [row for row in reader]

    data3=Card.objects.get(id=num)

    ctex1=cardmean1[data3.card1+78]
    ctex2=cardmean1[data3.card2+78]
    ctex3=cardmean1[data3.card3+78]
    ctex4=cardmean1[data3.card4+78]
    ctex5=cardmean1[data3.card5+78]
    ctex6=cardmean1[data3.card6+78]
    ctex7=cardmean1[data3.card7+78]
    ctex8=cardmean1[data3.card8+78]
    ctex9=cardmean1[data3.card9+78]
    ctex10=cardmean1[data3.card10+78]
    ctex11=cardmean1[data3.card11+78]
    ctex12=cardmean1[data3.card12+78]
    ctex13=cardmean1[data3.card13+78]
    chtml1=cardname[data3.card1+78]
    chtml2=cardname[data3.card2+78]
    chtml3=cardname[data3.card3+78]
    chtml4=cardname[data3.card4+78]
    chtml5=cardname[data3.card5+78]
    chtml6=cardname[data3.card6+78]
    chtml7=cardname[data3.card7+78]
    chtml8=cardname[data3.card8+78]
    chtml9=cardname[data3.card9+78]
    chtml10=cardname[data3.card10+78]
    chtml11=cardname[data3.card11+78]
    chtml12=cardname[data3.card12+78]
    chtml13=cardname[data3.card13+78]
    params={
        'login_user':request.user,
        'data3':data3,
        'id':num,
        'chtml1':chtml1,
        'chtml2':chtml2,
        'chtml3':chtml3,
        'chtml4':chtml4,
        'chtml5':chtml5,
        'chtml6':chtml6,
        'chtml7':chtml7,
        'chtml8':chtml8,
        'chtml9':chtml9,
        'chtml10':chtml10,
        'chtml11':chtml11,
        'chtml12':chtml12,
        'chtml13':chtml13,
        'ctex1':ctex1,
        'ctex2':ctex2,
        'ctex3':ctex3,
        'ctex4':ctex4,
        'ctex5':ctex5,
        'ctex6':ctex6,
        'ctex7':ctex7,
        'ctex8':ctex8,
        'ctex9':ctex9,
        'ctex10':ctex10,
        'ctex11':ctex11,
        'ctex12':ctex12,
        'ctex13':ctex13,
    }
    return render(request,'tarot/answer.html',params)




def get_your_group_message(owner, page):
    page_num = 10 

    messages = Card.objects.filter()
    page_item = Paginator(messages, page_num)
    return page_item.get_page(page)



from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm


class ContactFormView(LoginRequiredMixin, FormView):
    template_name = "tarot/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("result")

    def form_valid(self, form):
        form.send_email(
            login_use=self.request.user.username, 
        )
        return super().form_valid(form)

@login_required(login_url='/accounts/login/')
def result(request):
    params={
        'login_user':request.user,
    }
    return render(request,'tarot/result.html',params)



# #テスト
def test(request):
    data3=get_data3(request.user, 1)
    params={
        'login_user':request.user,
        'data':data3,
    }
    return render(request,'tarot/test.html',params)

def test1(request):
    html='https://www.yahoo.co.jp/'
    params={
        'login_user':request.user,
        'html':html,
    }
    return render(request, 'tarot/test1.html',params)



