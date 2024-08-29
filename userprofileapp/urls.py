from django.urls import path
from . import views

urlpatterns = [

    path("registration/",views.registration,name="registration"),
    path("",views.loginuser,name="login"),

    path("logout/",views.logout,name="logout"),
    path('userindex',views.userindex, name='userindex'),
    path('profile_form/',views.profile_form,name='profile_form'),
    path('project_form/',views.project_form,name='project_form'),
    path('listinfo',views.listinfo,name='listinfo'),
    path('updateinfo',views.updateinfo,name='updateinfo'),
    path('listproject', views.listproject, name='listproject'),
    path('updateproject/<int:project_id>/', views.updateproject, name='updateproject'),

    path("projectdetails/<int:project_id>/", views.projectdetails, name='details'),
    path('deleteproject/<int:project_id>/',views.deleteproject,name='delete'),
    path('updateproject/<int:project_id>/',views.updateproject,name='update'),
    path('updateskill/<int:skill_id>/', views.updateskill, name='updateskill'),
    path('createprofile/',views.createprofile,name='createprofile'),
    path('add_skill/', views.add_skill, name='add_skill'),
    path('listskill/', views.listskill, name='listskill'),
    path('deleteskill/<int:skill_id>/', views.deleteskill, name='deleteskill'),


]