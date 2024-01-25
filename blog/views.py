from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event


class EventList(generic.ListView):
    '''
    Code copied from Code Institute walktrough:
    https://github.com/Code-Institute-Solutions/Django3blog/tree/master/11_messages/blog
    I change the pagination number and names to suit this project.
    '''
    model = Event
    queryset = Event.objects.filter(status=1).order_by('created_on')
    template_name = 'blog/index.html'
    paginated_by = 3


class EventDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event_instance = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/event_detail.html",
            {
                "event": event_instance,
            },
        )


def home(request):
    """
    Renders the Homs page of the project.
    """
    return render(
        request,
        "blog/index.html")


def about(request):
    """
    Renders the About page of the project.
    """
    return render(
        request,
        "about.html")
