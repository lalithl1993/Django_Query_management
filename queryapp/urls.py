from django.conf.urls import url
from queryapp.views import *

urlpatterns = [
    url(r'^index/',index),
    url(r'^tr_login/',tr_login),
    url(r'^st_login/',st_login),
    # url(r'^teacher/',teacher),
    # url(r'^viewall/',all),
    # url(r'^new/',loginadd),
    url(r'^tr_add/',tr_add),
    url(r'^st_ask/',st_ask),
    url(r'^tr_disp/',tr_disp,name="list"),
    url(r'^tr_question/',tr_question),
    url(r'^tr_answer/',tr_answer),
    url(r'^(?P<id>\d+)/tr_edit/',tr_edit,name='update'),
    url(r'^(?P<id>\d+)/tr_delete/',tr_delete),
    url(r'^tr_history/',tr_history),
    url(r'^st_history/',st_history),
    #url(r'^testing/',testing),

]
