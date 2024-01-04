from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('created_on')
    template_name = 'blog/index.html'
    paginated_by = 6

class EventDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event_instance = get_object_or_404(queryset, slug=slug)
        # comments = post.comments.filter(approved=True).order_by("-created_on")
        # liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        return render(
            request,
            "blog/event_detail.html",
            {
                "event": event_instance,
            },
        )

def home(request):
    """This function render the about page of the project."""
    return render(
        request,
        "blog/index.html")
        
def about(request):
    """This function render the about page of the project."""
    return render(
        request,
        "about.html")


    

