from django.urls import path
from .views import ActivityList

urlpatterns = [
    path('list/', ActivityList.as_view(), name='list'),
]
