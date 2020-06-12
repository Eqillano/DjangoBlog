from django.urls import path


from .views import *

urlpatterns = [
  path('',home.as_view(),name='home'),
  path('category/<str:slug>/'),get_category,name='category')
  path('post/<str:slug>/',post_detail,name='detail')
]
