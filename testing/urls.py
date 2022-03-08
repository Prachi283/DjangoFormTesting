
from django.urls import path
from .views import home,home_view
urlpatterns = [
    path('home/',home),
    path('home_view/',home_view)

]
