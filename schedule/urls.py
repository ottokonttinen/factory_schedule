from django.urls import path
from .views import *

urlpatterns = [
    path('', ScheduleView.as_view()),
]
