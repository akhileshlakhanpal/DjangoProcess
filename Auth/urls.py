from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home,name='home'),
    path('signin', views.signin,name='signin'),
    path('signout', views.signout,name='signout'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('createproject', views.createproject, name = 'createproject'),
    path('projectdetails', views.projectdetails, name = 'projectdetails'),
    path('secondaryres/<int:id>',views.secondaryres,name='secondaryres'),
    path('datateam/<int:id>',views.datateam,name='datateam'),
    # path('ajax/get-options/', views.get_options, name='ajax_get_options'),
    path('success', views.success, name = 'success'),
    path('datagen', views.datagen,name='datagen'),
    path('export', views.export, name='export'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)