from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt  
from . import views


urlpatterns = [
    #Apps
    path('apps/', views.appListView.as_view(), name="Apps-Basic-Url"),
    path('apps/new', views.app_list),
    path('apps/<int:pk>', views.app_details),
    path('apps/newest', views.newestAppsListView.as_view()),
    path('apps/oldest', views.oldestAppsListView.as_view()),
    path('apps/mostdownloads', views.mostDownloadsListView.as_view()),
    path('apps/lessdownloads', views.tinyDownloadsListView.as_view()),
    path('apps/newcomments', views.newComments, name="newComment"),
    path('apps/changecomment', views.changecomment, name="changecomment"),
    
    #User/Permission
    path('users/', views.UserListView.as_view(), name="Basic_user_url"),
    path('users/new', views.createUser, name="new User")
]