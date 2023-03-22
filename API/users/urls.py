from django.urls import path

from . import views

##End points for user data
app_name = 'users'
urlpatterns = [
    ##Endpoint for all user data
    path('<current_username>/', views.getUserProfileData, name='getUserProfileData'),
    ##Endpoint for verifing the users account
    path('<username>/verify/', views.verifyAccount, name='verifyAccount'),
    ##Endpoint for adding xp for when a user filles a bottle
    path('fillBottle/<current_username>/<building_name>/', views.bottleFilled, name='bottleFilled'),
    ##Endpoint for setting a users name
    path('<current_username>/setName/<new_name>/', views.setName, name='setName'),
    ##Endpoint for registering a user
    path('register', views.index, name='register'),
    ##Endpoint for registering a user
    path('setPic/<name>/<type>/', views.SetUserPic.as_view(), name='index'),
    # Endpoint to get data for an authorised user
    path('data', views.AuthGetUserData.as_view(), name='authGetUserProfileData')
]