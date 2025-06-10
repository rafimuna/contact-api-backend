from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Contact
from .serializers import ContactSerializer

class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
