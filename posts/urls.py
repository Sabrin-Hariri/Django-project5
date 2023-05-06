from django.contrib import admin
from django.urls import path ,include
# from .views import * 
from . import views
from rest_framework import routers


router= routers.DefaultRouter()
router.register('post',views.PostView)

urlpatterns = [
     path('', include(router.urls) ),
#    path('post/', viewsets.PostView() , name="post" ),
#    path('snippets/<int:pk>/', viewsets.snippet_detail),

]
