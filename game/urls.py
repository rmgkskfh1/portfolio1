from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.puz_list, name='puz_list'),
    url(r'^game/game1', views.game1, name='game1'),
    url(r'^game/game2', views.game2, name='game2'),
    url(r'^game/score_list', views.score_list, name='score_list'),
    url(r'^ajax/validate_score/$', views.validate_score, name="validate_score"),
    url(r'^ajax/validate_scoreupdate/$', views.validate_scoreupdate, name="validate_scoreupdate"),
    url(r'^ajax/game1score_list/$', views.game1score_list, name="game1score_list"),

]

