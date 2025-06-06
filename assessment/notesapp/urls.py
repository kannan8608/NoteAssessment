from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('user/', views.UsersDetails.as_view(),name='user'),
    path('note/', views.NotesDetails.as_view(),name='note'),
    path('success/', views.success,name='success'),
    path('renote/', views.re_enter_notes,name='renote'),
    path('note_success/', views.notes_success,name='note_success')
]