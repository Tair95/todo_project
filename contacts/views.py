from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


def contact_list(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts, 'form': form})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contact_list')


def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/edit_contact.html', {'form': form, 'contact': contact})


