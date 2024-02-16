from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from Common.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView
@api_view(http_method_names=['GET','POST'])
def get_profile(request):
    if request.method == 'POST':
        print(request.data)
        print(type(request.data))
    profile = Profile.objects.first()
    data = {
        'image': str(profile.image),
        'full_name': profile.full_name,
        'bio': profile.bio
    }
    return Response(data=data, status=200)

class ProfileDate(APIView):

    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        profile = Profile.objects.first()
        data = {
            'image': str(profile.image),
            'full_name': profile.full_name,
            'bio': profile.bio
        }
        return Response(data=data, status=200)
    def post(self,request,format=None):
        print(request.data)
        return Response( status=200)
    

@api_view()
def get_skill(request):
    skills = Skill.objects.all()
    result = []
    for skill in skills :
        a ={
        'title': skill.title,
        'percentage': skill.percentage
        }
        result.append(a)
    return Response(result)

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = ("title", "percentage")
class SkillData(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request , format=None):
        skills = Skill.objects.all()
        serializer = SkillSerializer(instance=skills , many=True)
        return Response(serializer.data)
    
class AboutData(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        about = About.objects.first()
        data ={
            'experience': about.experience,
            'total_project': about.total_project,
            'total_users': about.total_users,
        }
        return Response(data=data, status=200)
    def post(self,request,format=None):
        print(request.data)
        return Response( status=200)
    
class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ("title", "icon", "description")

class ServiceListAPIiew(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def post(self,requast,format=None) :
        print(requast.data)
        return Response( status=200)

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)

class CategoryListAPIView(ListAPIView) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def post(self,requast,format=None) :
        print(requast.data)
        return Response( status=200)
class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ("title", "description", "image", "link", "used_tools","category","completed_at")

class PortfolioListAPIView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    def post(self,requast,format=None) :
        print(requast.data)
        return Response( status=200)

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "description", "author", "image", "view_counts", "id")

class PostListAPIiev(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def post(self,requast,format=None) :
        print(requast.data)
        return Response( status=200)



        

    