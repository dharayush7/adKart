from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.index, name="contact"),
    path("track/", views.index, name="track"),
    path("search/", views.index, name="search"),
    path("product-view/", views.index, name="productView"),
    path("checkout/", views.index, name="checkout"),

]
