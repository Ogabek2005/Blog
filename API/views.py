from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from Common.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer

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
class SkillDate(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request , format=None):
        skills = Skill.objects.all()
        serializer = SkillSerializer(instance=skills , many=True)
        return Response(serializer.data)


    