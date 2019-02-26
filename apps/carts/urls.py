from django.conf.urls import url
from django.contrib import admin

from carts import views

urlpatterns = [
    url(r'^carts/count/$', views.CartsCountView.as_view()),
]

