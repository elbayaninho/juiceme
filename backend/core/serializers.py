from rest_framework import serializers
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from phonenumber_field.serializerfields import PhoneNumberField

from core.models import *


class CandidateSerializer(serializers.ModelSerializer):
    #This url will allow the click and getting the details of the candidates 
    url = serializers.HyperlinkedIdentityField(view_name='candidate-detail', lookup_field = 'pk')

    #This url will allow the edit of the candidate details 
    edit_url = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Candidate
        fields = ['edit_url', 
                  'url','pk', 'first_name', 'middle_name', 'last_name',
                  'dob', 'gender', 'maritual_status',
                  'prefered_industry', 'salary_expectation', 'education_level',
                  'skills', 'Experience', 'language']
        
    
    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('candidate-update',kwargs={"pk":obj.pk},request=request)
    

    def create(self, validated_data):
        #Add other activities that are required before the process of saving to the data base
        #Here we can initiate other activities that deals with other serializers
        return super().create(validated_data)
    

    def update(self, instance, validated_data):
        #Similarly here we will do another activities that are happening before we update the models 
        #This can also be done within the serializer class it self
        return super().update(instance, validated_data)



class CandidateFileSerializer(serializers.ModelSerializer):
    class Meta: 
        model  = Candidate
        fields = ['first_name', 'last_name', 'dob', 'gender', 'maritual_status']
        

class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class User1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class EmployerHRSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()

    class Meta:
        model = EmployerHR
        fields = ['id', 'user', 'company', 'phone_number', 'address', 'dob', 'designation']
