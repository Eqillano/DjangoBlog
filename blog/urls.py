from django.urls import path


from .views import *

urlpatterns = [
  path('',Home.as_view(),name='home'),
  path('category/<str:slug>/',PostByCategory.as_view(),name='category'),
  path('post/<str:slug>/',PostDetail.as_view(),name='post'),

]
