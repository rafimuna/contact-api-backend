# contacts/views.py

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contact
from .serializers import ContactSerializer
from .pagination import ContactPagination  # You’ll create this file below

# 📄 List View with Filtering, Searching, Pagination
class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = ContactPagination  # Custom pagination class

    # 🔍 Filter, Search, Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'email']  # filter by exact match
    search_fields = ['name', 'email', 'message']  # search by partial match
    ordering_fields = ['name', 'email', 'id']  # sort by any field

# ✉️ Create View for adding a contact
class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
