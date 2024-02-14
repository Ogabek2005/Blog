from django.urls import path
from .views import *

urlpatterns = [
    path("profile/",ProfileDate.as_view()),
    path("skill/",SkillDate.as_view()),
]