from django.conf.urls import url
from blog_app import views

urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name='about'),
]