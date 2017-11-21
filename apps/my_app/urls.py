from django.conf.urls import url, include
from . import views 



urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit_word$', views.submit_word),
    url(r'^result$', views.result),
    url(r'^clear$', views.clear),
    
]