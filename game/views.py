from django.shortcuts import render
from django.utils import timezone
from .models import Puzzle
from .models import History
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

def puz_list(request):
    return render(request, 'game/puz_list.html', {})



def validate_score(request):

    player = request.GET.get('player', None)
    u = User.objects.get(id=player)
    q = History.objects.filter(author=u, gametitle='game1')
    
    data = {

        'score':q.last().score
    }

    return JsonResponse(data)

def validate_scoreupdate(request):

    player = request.GET.get('player', None)
    scoredata = request.GET.get('scoredata', None)
    gametitle = request.GET.get('gametitle', None)
    u = User.objects.get(id=player)
    History.objects.create(author=u, gametitle=gametitle, score=scoredata, savedata= 'level:3')
    q = History.objects.filter(author=u)
    w = q.last()
    w.score = scoredata
    w.save()
    data = {

        'score':w.score
    }

    return JsonResponse(data)

def game1score_list(request):
    

    game123 = request.GET.get('game', None)
    user = request.GET.get('user', None)
    #num = int(request.GET.get('num', None))
    qwe=History.objects.filter(gametitle=game123).order_by('-score')
    scoredata="<thead><tr><th>순위</th><th>id</th><th>점수</th><th>기록날짜</th></tr></thead><tbody>"
    for i in range(len(qwe)):
        if str(qwe[i].author)==user:
            scoredata=scoredata+"<tr class='info'>"+"<td>"+str(i+1)+"등"+"</td>"
        else:
            scoredata=scoredata+"<tr class='active'>"+"<td>"+str(i+1)+"등"+"</td>"
        scoredata=scoredata+"<td>"+str(qwe[i].author)+"</td>"
        scoredata=scoredata+"<td>"+str(qwe[i].score)+"</td>"
        scoredata=scoredata+"<td>"+str(qwe[i].created_date)+"</td>"
        scoredata=scoredata+"</tr>"
    scoredata+="</tbody>"

    data = {

        'scoredata':scoredata
    }

    return JsonResponse(data)


def game1(request):
    return render(request, 'game/game1.html', {})

@login_required
def score_list(request):
    return render(request, 'game/score_list.html', {})


def game2(request):
    return render(request, 'game/game2.html', {})