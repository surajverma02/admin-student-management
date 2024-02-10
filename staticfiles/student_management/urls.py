"""
URL configuration for student_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from student.views import *
# for use of media directory
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage, name="main"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('home/', homePage, name="home"),
    path('delete/<str:pk>', deleteStudent, name="delete"),
    path('add-student/', addStudent, name="addStudent"),
    path('update-student/<str:pk>', updateStudent, name="updateStudent"),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
