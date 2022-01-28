from django.contrib import admin


from bookstore.models.BookStore import BookStore
from bookstore.models.GuitarStore import GuitarStore
from bookstore.models.FoodchainStore import FoodchainStore
from bookstore.models.ClothingStore import ClothingStore
from bookstore.models.SneakersStore import SneakersStore
from bookstore.models.CarStore import CarStore
from bookstore.models.MusicStore import MusicStore
from bookstore.models.ArtStore import ArtStore
from bookstore.models.KpopStore import KpopStore
from bookstore.models.BagStore import BagStore

# Register your models here.
admin.site.register(BookStore)
admin.site.register(GuitarStore)
admin.site.register(FoodchainStore)
admin.site.register(ClothingStore)
admin.site.register(SneakersStore)
admin.site.register(CarStore)
admin.site.register(MusicStore)
admin.site.register(ArtStore)
admin.site.register(KpopStore)
admin.site.register(BagStore)