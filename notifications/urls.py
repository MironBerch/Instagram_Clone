from django.urls import path
from .views import *


urlpatterns = [
    path('', name='show-notifications'),
    path('<noti_id>/delete', name='delete-notifications')
]