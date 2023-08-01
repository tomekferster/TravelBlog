from django.shortcuts import render
from .models import TravelPost
# Create your views here.

# authors = [
#     {'id': 1, 'name': 'Bobby'},
#     {'id': 2, 'name': 'Tony'},
#     {'id': 3, 'name': 'Andy'},
# ]

def home(request):
    print(request)
    travel_posts = TravelPost.objects.all()
    context = {'travel_posts':travel_posts}
    return render(request, 'base/home.html', context)


def travel_post(request, pk):
    travel_post = None
    travel_post = TravelPost.objects.get(pk=pk)
    context = {'travel_post': travel_post}

    return render(request, 'base/travel_post.html', context)


def contact(request):
    if request.method == 'POST':
        print(request.POST.get('firstname'))
    return render(request, 'base/contact.html')