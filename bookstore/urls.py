"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from bookstore.views.bookstoreviews import BookStoreGet
from bookstore.views.guitarstoreviews import GuitarStoreGet
from bookstore.views.foodchainviews import FoodchainStoreGet
from bookstore.views.clothingstoreviews import ClothingStoreGet
from bookstore.views.sneakersstoreviews import SneakersStoreGet
from bookstore.views.carstoreviews import CarStoreGet
from bookstore.views.musicstoreviews import MusicStoreGet
from bookstore.views.artstoreviews import ArtStoreGet
from bookstore.views.kpopstoreviews import KpopStoreGet
from bookstore.views.bagstoreviews import BagStoreGet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookstore/', BookStoreGet.as_view()),
    path('bookstore/', GuitarStoreGet.as_view()),
    path('foodchainstore/', FoodchainStoreGet.as_view()),
    path('clothingstore/', ClothingStoreGet.as_view()),
    path('sneakersstore/', SneakersStoreGet.as_view()),
    path('carstore/', CarStoreGet.as_view()),
    path('musicstore/', MusicStoreGet.as_view()),
    path('artstore/', ArtStoreGet.as_view()),
    path('artstore/', KpopStoreGet.as_view()),
    path('bagstore/', BagStoreGet.as_view()),
]
