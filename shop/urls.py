from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('contact/success', views.contactSuccess, name="contactSuccess"),
    path("track/", views.tracker, name="track"),
    path("search/", views.index, name="search"),
    path("product/<int:id>", views.product, name="productView"),
    path("checkout/", views.index, name="checkout"),

]
