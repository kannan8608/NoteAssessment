from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
import datetime
from django.utils import timezone
from django.template import loader
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')

def re_enter_notes(request):
    return render(request, 'notes.html')

def success(request):
    return render(request, 'success.html')
def notes_success(request):
    return render(request, 'notes_success.html')

# Create your views here.
class UsersDetails(APIView):
    permission_classes = [AllowAny,]
    def get(self,request):
        try:
            data=request.query_params
            user_email=data.get('user_email')
            user_password=data.get('user_password')
            
            try:
                user_obj = Users.objects.get(user_email=user_email,user_password=user_password)
                return Response({"status":"success","message":"Data created successfully","data":{"user_name":user_obj.user_name,"user_mail":user_obj.user_email,"last_update":user_obj.last_update}},status=status.HTTP_200_OK)
            except:
                return Response({"status":"error","message":"Something went wrong "+str(e)},status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"status":"error","message":"Something went wrong "+str(e)},status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            data=request.data
            user_name=data.get('user_name')
            user_email=data.get('user_email')
            user_password=data.get('user_password')
            #super user api creation
            if not User.objects.filter(username=user_name).exists():
                test=User.objects.create_user(username=user_name, password=user_password,email=user_email,first_name=user_name, is_active=True)
            user_obj = Users(user_name=user_name,user_email=user_email,user_password=user_password)
            user_obj.save()
            return render(request, 'success.html')
            # return Response({"status":"success","message":"Data created successfully","data":user_obj.id},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"error","message":"Something went wrong "+str(e)},status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        try:
            data=request.data
            user_id=data.get('user_id')
            user_name=data.get('user_name')
            user_email=data.get('user_email')
            user_password=data.get('user_password')
            try:
                user_obj = Users.objects.get(id=user_id)
            except:
                return Response({"status":"error","message":"User not found","data":None},status=status.HTTP_400_BADRREQUEST)
            user_obj.user_email=user_email
            user_obj.user_password=user_password
            user_obj.user_name=user_name
            user_obj.last_update=datetime.datetime.now(tz=timezone.utc)
            user_obj.save()
            return Response({"status":"success","message":"Data updated successfully","data":user_obj.id},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"error","message":"Something went wrong "+str(e)},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        try:
            data=request.data
            user_id=data.get('user_id')
            try:
                user_obj = Users.objects.get(id=user_id)
            except:
                return Response({"status":"error","message":"User not found","data":None},status=status.HTTP_400_BADRREQUEST)
            user_obj.last_update=datetime.datetime.now(tz=timezone.utc)
            user_obj.is_active=False
            user_obj.save()
            return Response({"status":"success","message":"Data deleted successfully","data":user_obj.id},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"error","message":"Something went wrong "+str(e)},status=status.HTTP_400_BAD_REQUEST)

class NotesDetails(APIView):
    
    def get(self,request):
        try:
            details=[]
            data=request.query_params
            note_id=data.get('notes_id',None)
            if note_id is not None:
                note_obj = [Notes.objects.get(id=note_id)]
            else:
                note_obj = Notes.objects.all()
            for obj in note_obj:
                details.append({
                    'id':obj.id,
                    'notes_title':obj.notes_title,
                    'notes_content':obj.notes_content,
                    'create_on':obj.create_on,
                    
                })
            return Response({"status":"success","message":"Data fetched successfully","data":details},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"error","message":"Something went wrong "+str(e)},status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            data=request.data
            notes_title=data.get('notes_title')
            notes_content=data.get('notes_content')
            notes_obj = Notes(notes_title=notes_title,notes_content=notes_content)
            notes_obj.save()
            return Response({"status":"success","message":"Data updated successfully","data":notes_obj.id},status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"status":"error","message":"Something went wrong "+str(e)},status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        try:
            data=request.data
            notes_id=data.get('notes_id')
            notes_title=data.get('notes_title')
            notes_content=data.get('notes_content')
            try:
                notes_obj = Notes.objects.get(id=notes_id)
            except:
                return Response({"status":"error","message":"User not found","data":None},status=status.HTTP_400_BAD_REQUEST)
            notes_obj.last_update=datetime.datetime.now(tz=timezone.utc)
            notes_obj.notes_title=notes_title
            notes_obj.notes_content=notes_content
            notes_obj.save()
            return Response({"status":"success","message":"Data updated successfully","data":notes_obj.id},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"error","message":"Something went wrong "+str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request):
        try:
            data=request.data
            notes_id=data.get('notes_id')
            try:
                notes_obj = Notes.objects.get(id=notes_id)
            except:
                return Response({"status":"error","message":"User not found","data":None},status=status.HTTP_400_BAD_REQUEST)
            notes_obj.is_active=False
            notes_obj.last_update=datetime.datetime.now(tz=timezone.utc)
            notes_obj.save()
            return Response({"status":"success","message":"Data deleted successfully","data":notes_obj.id},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"error","message":"Something went wrong "+str(e)},status=status.HTTP_400_BAD_REQUEST)


