from .models import Contact, AddressBook
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.




class ContactsListView(ListView):
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


class ContactCreateView(CreateView):
    ...


class ContactDeleteView(DeleteView):
    ...


class ContactUpdateView(UpdateView):
    ...

