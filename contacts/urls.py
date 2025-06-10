from django.urls import path
from .views import ContactCreateAPIView, ContactListView  # import your actual views here

urlpatterns = [
    path('', ContactListView.as_view()),  # directly use the class
    path('create/', ContactCreateAPIView.as_view(), name='contact-create'),
]
