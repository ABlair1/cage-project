from django.urls import path

from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('entry/<int:pk>', views.CatalogEntryView.as_view(), name='catalog-entry'),
]
