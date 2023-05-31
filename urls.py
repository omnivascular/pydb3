"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

app_name = "pydbapp"
urlpatterns = [
    path("search_products", views.search_products, name="search_products"),
    path("home", views.home, name="home"),
    path("", views.IndexView.as_view(), name="index"),
    path("product/search/<int:pk>/", views.search_product, name="search-product"),
    path("products/", views.ProductHomeView.as_view(), name="products"),
    path("vendors/", views.VendorHomeView.as_view(), name="vendors"),
    path("admin/", admin.site.urls),
]

urlpatterns += [
    # path("product/<int:pk>/search", views, name="search-product"),
]
