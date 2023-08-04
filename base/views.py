from django.shortcuts import render, get_object_or_404
from .models import TravelPost
from .forms import TravelPostForm
# Create your views here.


def home(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    travel_posts = TravelPost.objects.all()
    posts_per_page = 10
    context = {
        'travel_posts':travel_posts,
        'posts_per_page': posts_per_page
    }
    return render(request, 'base/home.html', context)


def travel_post(request, pk):
    travel_post = get_object_or_404(TravelPost, pk=pk)
    comments = travel_post.comment_set.all()            # accessing child class 
    comments_num = len(travel_post.comment_set.all())
    # tags = travel_post.tags.all()                     # accessing many to many relation classes, done on the template side
    context = {
        'travel_post': travel_post,
        'comments': comments,
        'comments_num': comments_num,
        }
    return render(request, 'base/travel_post.html', context)


def create_travel_post(request):
    form = TravelPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    return render(request, 'base/travel_post_form.html', context)


def contact(request):
    if request.method == 'POST':
        print(request.POST.get('firstname'))
    return render(request, 'contact.html')