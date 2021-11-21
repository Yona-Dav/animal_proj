from django.urls import path
from . import views
# from .views import redirect_view

urlpatterns = [
    path('animal/<int:animal_id>/', views.animal),
    path('family/<int:family_id>/', views.family),
    path('animals/', views.animals)
]