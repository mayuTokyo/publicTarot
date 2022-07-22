from django.urls import URLPattern, path
from . import views
from django.views.generic import TemplateView   # 追加

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:page>',views.index,name='index'),
    path('start',views.start,name='start'),
    path('test',views.test,name='test'),
    path('test1',views.test1,name='test1'),
    path('past',views.past,name='past'),
    path('answer/<int:num>',views.answer,name='answer'),
    path('point/<int:num>',views.point,name='point'),
    path('point1/<int:num>',views.point1,name='point1'),
    path("contact/", views.ContactFormView.as_view(), name="contact"),   # フォーム
    path("result", views.result,name="result"),   # 完了画面  
]