from django.shortcuts import render, redirect
from django.contrib import messages
from contacts.models import Contact
from contacts.forms import ContactForm
# Create your views here.

def contacts_index(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact added")

            return redirect("contacts_index_page")

    form = ContactForm()
    contacts = Contact.objects.all()
    
    return render(request, 'contacts/index.html', {
        "contacts" : contacts,
        "form" : form
    })


def contacts_show(request, id):
    try:
        contact = Contact.objects.get(pk=id)
    except:
        messages.error(request, "LOL showing contact spoil")
        return redirect("contacts_index_page")

    form = None

    if request.GET.get("edit") == "true":
        form = ContactForm(instance=contact)

    if request.GET.get("edit") == "true" and request.method =="POST":
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            messages.success(request, "Contact has been edited.")

            return redirect('contacts_index_page')

    if request.GET.get("delete") == "true" and request.method == "POST":
        contact.delete()
        messages.success(request, "Contact has said bye bye and cannot find any more")

        return redirect("contacts_index_page")

    return render(request, "contacts/show.html", {"contact" : contact, "form": form})

    