from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Master, TextEntry

word_dict = dict()  # persistent context


def index(request):
    """
    Creates and returns an index HTML page
    :param request: The http request
    :return: an HTML page
    """
    current_stories_list = Master.objects.order_by('-story_name')[:]
    context = {'current_stories_list': current_stories_list}
    return render(request, 'madlibs/index.html', context)


def input(request, master_id):
    """
    Creates and returns an input HTML page.
    :param request: The http request
    :param master_id: The id for a specific story
    :return: an HTML page
    """
    master = get_object_or_404(Master, pk=master_id)
    try:
        selected_textentry = master.textentry_set.get(pk=request.POST['textentry'])
    except (KeyError, TextEntry.DoesNotExist):
        # Redisplay the same input page with an error message
        context = {'master': master,
                   'error_message': "Please select a word."}
        return render(request, 'madlibs/input.html', context)
    else:
        word_dict["selected_textentry"] = selected_textentry
        return HttpResponseRedirect(reverse('madlibs:results', args=(master.id,)))



def results(request, master_id):
    """
    Creates and returns a result HTML page.
    :param request: The http request
    :param master_id: The id for a specific story
    :return: an HTML page
    """
    master = get_object_or_404(Master, pk=master_id)
    word_dict['master'] = master
    return render(request, 'madlibs/results.html', word_dict)
