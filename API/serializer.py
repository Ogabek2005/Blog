from rest_framework.serializers import ModelSerializer , Serializer
from Common.models import *
from rest_framework.generics import *
from rest_framework import serializers

class SkillSerilizer(ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"
        read_only = ("id","created_at","updated_at")


class AboutSerilizer(Serializer):
    experience = serializers.CharField()
    salary = serializers.IntegerField()
    total_users = serializers.IntegerField()
    total_project = serializers.IntegerField()




    def validate(self, attrs):
        print(attrs)
        if attrs["salary"] < 1000:
            raise serializers.ValidationError(detail={
                'salary':"1000 som dan kam qilish mumkin emas"
            },code=400)
        if attrs["total_users"] < attrs["total_project"]:
            raise serializers.ValidationError(detail={
                'total_users':"total_users kam qilish mumkin emas"
            },code=400)

        return super().validate(attrs)

    def create(self, validated_data):
        # print(validated_data)
        
        
        about = About.objects.create(
            **validated_data
        )
        return about












