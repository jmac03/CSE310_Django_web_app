from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import TextField
# Create your views here.
def index(request):
    latest_entry_list = TextField.objects.order_by('-id')[:5]
    context = {
        'latest_entry_list': latest_entry_list,
    }
    return render(request, 'madlibs/index.html', context)

def input(request, entry_id):
    # this is similar to vote in the tutorial
    entry = get_object_or_404(TextField, pk=entry_id)
    try:
        # Next line gets a string value when an integer is expected
        # 'input' is the name defined in the html template page for the text input box
        # TextField is generic,lookign at all text fields.
        # when I enter the current text, then this l;ine of code works, showing the results page
        selected_input = TextField.objects.get(id=request.POST['input'])  # entry instead of input
        # entry_input = entry.entry_set.get(pk=request.POST['entry'])  # I am having trouble getting the entry text from the user's html page
        # print(selected_input)
    except (KeyError, TextField.DoesNotExist):
        context = {'entry': entry, 'error_message': "You did not put anything in the text field.",}
        return render(request, 'madlibs/input.html', context)
    else:
        selected_input.entry_text = selected_input.entry_text
        selected_input.save()
        # entry_input.entry_text = 
        return HttpResponseRedirect(reverse('results', args=(entry.id,)))
        # context =  {'entry': entry}
        # return render(request, 'madlibs/input.html', context)


"""def detail(request, entry_id):
    entry = get_object_or_404(TextField, pk=entry_id)
    context =  {'entry': entry}
    return render(request, 'madlibs/detail.html', context)"""

# Does this even need entry_id?
def results(request, entry_id):
    # eventually you will return an html page full of the text entries
    try:
        entry = TextField.objects.get(pk=entry_id)
    except TextField.DoesNotExist:
        raise Http404("TextField does not exist")
    return render(request, 'madlibs/results.html', {'entry': entry}) # this line should error. detail.html does not yet exist.
    # return HttpResponse("You are lookign at the results of all your text entries.")