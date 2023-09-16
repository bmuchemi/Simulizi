from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name= 'home'),
    path('view/', views.about, name='about'),
    path('story/',views.story_list, name='story_list'),
    path('poem/',views.poem_list, name='poem_list'),
    path('story/<int:story_id>/', views.story_detail, name='story_detail'),
    path('poem/<int:poem_id>/', views.poem_detail, name='poem_detail'),
    path('sports/',views.sports_view,name='sports_view'),
    path('sports/<int:desk_id>/',views.sports,name='sports'),
    ]