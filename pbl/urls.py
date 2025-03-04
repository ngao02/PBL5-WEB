"""pbl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path
from . import views
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$',views.login),
    re_path(r'^postsign/',views.postsign),
    re_path(r'^logout/',views.logout, name='logout'),
    re_path(r'^signUp/',views.signUp,name='signUp'),
    re_path(r'^postsignUp/',views.postsignUp,name='postsignUp'),
    re_path(r'^setting/',views.setting,name='setting'),
    re_path(r'^postUpdate/',views.postUpdate,name='postUpdate'),
    re_path(r'^postCancel/',views.postCancel,name='postCancel'),
]
