from django.urls import path
from django.views.generic import TemplateView
# from django.conf.urls import include, url
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('getInfo',views.getInfo,name='getInfo'),
    path('viewcitymap',views.viewcitymap,name='viewcitymap'),
    # url(r'^graph/', TemplateView.as_view(template_name="graph.html"),
                #    name='graph'),
]