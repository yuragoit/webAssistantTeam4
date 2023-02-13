from .models import Contact, AddressBook
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm
from django.urls import reverse_lazy
from apps.common.mixins import TitleMixin
from datetime import timedelta
from django.db.models.functions import Now


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
        queryset = queryset.filter(address_book=book)
        if self.request.POST.get('birthday_option'):
            in_days = int(self.request.POST.get('birthday_option')) - 1
            print(in_days)
            queryset = queryset.filter(birthday__gte=Now() + timedelta(days=in_days))
        return queryset

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


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

