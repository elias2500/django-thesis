from django.urls import re_path
from . import views

#template_urls
app_name = 'projects'

urlpatterns = [
    re_path(r'^user_login/$', views.user_login, name='user_login')
]
