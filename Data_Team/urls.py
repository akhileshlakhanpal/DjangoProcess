# from . import views
# from django.contrib import admin
# from django.urls import path,include
# from django.conf.urls.static import static
# from django.conf import settings
#
#
# urlpatterns = [
#     path('', views.home,name='home'),
#     path('signout', views.signout,name='signout'),
#     path('datateam', views.datateam,name='datateam'),
#     path('datagen', views.datagen,name='datagen'),
#     path('generatedata', views.generatedata,name='generatedata'),
#     path('export', views.export, name='export'),
#
#
# ]
#
# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)