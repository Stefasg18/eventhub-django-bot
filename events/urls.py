from django.urls import path
from . import views
urlpatterns=[path('',views.index,name='index'),path('api/events/',views.api_events,name='api_events')]
