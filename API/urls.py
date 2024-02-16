from django.urls import path
from .views import *

urlpatterns = [
    path("profile/",ProfileDate.as_view()),
    path("skill/",SkillData.as_view()),
    path("about/",AboutData.as_view()),
    path("service/",ServiceListAPIiew.as_view()),
    path("category/",CategoryListAPIView.as_view()),
    path("portfolio/",PortfolioListAPIView.as_view()),
    path("post/",PostListAPIiev.as_view()),
]