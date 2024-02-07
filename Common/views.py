from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    abouts = About.objects.all()
    services = Service.objects.all()
    posts = Post.objects.all()
    portfolio = Portfolio.objects.all()
    categories = Category.objects.first()
    context = {"profile":profile,
               "skills":skills,
               "abouts":abouts,
               "services":services,
               "posts":posts,
               "portfolio":portfolio,
               "categories":categories}
    return render(request,"index.html",context)

def about(request):
    abouts = About.objects.all()
    context = {"abouts":abouts}
    return render(request,"about-us.html" , context)
def portfolio(request):
    categories = Category.objects.first()
    portfolio = Portfolio.objects.all()
    context = {"categories" : categories,
               "portfolio" : portfolio
              }
    return render(request,"portfolio.html",context)
def blog(request):
    posts = Post.objects.all()
    if request.method == "POST":
        search = request.POST.get("search")
        if search:
            posts = Post.objects.filter(title__icontains=search)
    context = {
        "posts" : posts
    }
    return render(request,"blog.html",context)
def blog_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request,"single-blog.html",{'post':post})






def portfolio_details(request):
    categories = Category.objects.first()
    portfolio = Portfolio.objects.all()
    context = {"categories" : categories,
               "portfolio" : portfolio
              }
    return render(request,"portfolio-details.html",context)