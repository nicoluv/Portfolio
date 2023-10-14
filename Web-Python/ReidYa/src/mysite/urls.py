"""mysite URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from uploads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('mainpage', views.index, name="webform"),
    path('signatures/', views.signatures, name='signatures'),
    path('images/<str:folder>/', views.images, name='images'),
    path('docs/<str:folder>/', views.docs, name='docs'),
    path('reporte/', views.reporte, name='reporte'),
    path('people/', views.people, name='people'),
    path('people/<str:person_name>/', views.person, name='person'),
    path('people/<str:person_name>/<str:letter_name>/', views.letter, name='letter'),
    path('result', views.result, name="output"),
    path('maintenance/', views.under_maintenance, name='under_maintenance'),
    path('convert-to-pdf/', views.convert_to_pdf, name='convert_to_pdf'),

]


urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
)
