"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('person.urls')),
    path('play/', views.play, name = 'play'),
    # path('play/words.html', views.play_words, name = 'play_words'),
    path('result/',views.result, name = 'result'),
    path('modal/',views.modal,name='modal'),
    path('postresult/',views.postresult,name='postresult'),
    path('proceed/', views.proceed, name='proceed'),
    path('postanswer',views.postanswer,name='postanswer'),
    path('quesproceed',views.quesproceed,name='quesproceed')

] + static('/play/', document_root=settings.STATIC_ROOT)
