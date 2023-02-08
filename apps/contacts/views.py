from .models import Contact, AddressBook
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm
from django.urls import reverse_lazy
from apps.common.mixins import TitleMixin
# Create your views here.


class ContactsListView(TitleMixin, ListView):
    title = 'Contacts'
    template_name = 'contacts/contacts.html'
    model = Contact

    def get_queryset(self):
        try:
            book = AddressBook.objects.get(user=self.request.user)
        except:
            return None
        queryset = super().get_queryset()
        return queryset.filter(address_book=book)


class ContactCreateView(TitleMixin, SuccessMessageMixin, CreateView):
    title = 'Create contact'
    template_name = 'contacts/contact_add.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts:contact_list')

    def form_valid(self, form):
        book, _ = AddressBook.objects.get_or_create(user=self.request.user)
        form.instance.address_book = book
        return super().form_valid(form)


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:contact_list')


class ContactUpdateView(TitleMixin, UpdateView):
    title = 'Update Contact'
    template_name = 'contacts/contact_update.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts:contact_list')

