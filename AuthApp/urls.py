from .views import *
from django.urls import path
# from django.conf.urls import url
# from django.conf import settings

urlpatterns = [
    path('', register, name= 'register'),
    path('login/', login, name = 'login'),
    path('users/', index, name='index'),
    path('users/posts/', posts, name='posts'),
    path('users/logout/', logout, name='logout')
    # url(r'^logout/$', index, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]   