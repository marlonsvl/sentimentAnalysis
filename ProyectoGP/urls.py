"""ProyectoGP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mi_csv import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^$', views.url_lista, name="url_lista"),
    url(r'^normalizar$', views.index_normalizacion, name="index_normalizacion"),
    url(r'^sentiwordnet$', views.index_sentiwordnet, name="index_sentiwordnet"),
]
=======
    url(r'^$', views.index, name="index"),
] 
>>>>>>> 89fad760f1e1b6720622859fa8cca6decba210bf
