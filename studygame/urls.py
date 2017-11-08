#_*_ coding:utf-8 _*_
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'recognize_en_word/$', views.recognize_en_word, name='recognize_en_word' ),
    url(r'recognize_en_word_result/$', views.recognize_en_word_result, name='recognize_en_word_result' ),
    url(r'task_center',views.task_center,name='task_center'),
    url(r'do_task/', views.do_task, name='do_task' ),
    url(r'complete_task', views.complete_task, name='complete_task' ),
    url( r'player', views.player, name='player' ),
    url( r'hatch_en_word', views.hatch_en_word, name='hatch_en_word' ),
    url( r'save_en_word', views.save_en_word, name='save_en_word' ),
    url( r'shop', views.shop, name='shop' ),
    url( r'dictate_en_word/$', views.dictate_en_word, name='dictate_en_word' ),
    url( r'dictate_en_word_result/$', views.dictate_en_word_result, name='dictate_en_word_result' ),
    url( r'make_en_sentence/$', views.make_en_sentence, name='make_en_sentence' ),
    url( r'make_en_sentence_result/$', views.make_en_sentence_result, name='make_en_sentence_result' ),
    url( r'challenge_thirty_en_word/$', views.challenge_thirty_en_word, name='challenge_thirty_en_word' ),

]