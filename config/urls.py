from django.contrib import admin
from django.urls import path, include   #includeを追加
from django.views.generic import TemplateView  #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), #追加
    path('accounts/', include('allauth.urls')), #追加
    path('tarot/', include('app.urls')), #追加
]