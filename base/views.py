from django.shortcuts import render, get_object_or_404, redirect
from .models import TravelPost, Tag
from .forms import TravelPostForm, CommentForm
# Create your views here.


def home(request, *args, **kwargs):
    # print(request.user)
    # print(args, kwargs)
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
    new_comment = None

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = travel_post
            new_comment.save()
            return redirect('travel-post', pk=travel_post.pk)

    context = {
        'travel_post': travel_post,
        'comments': comments,
        'comments_num': comments_num,
        'form': form,
        }
    return render(request, 'base/travel_post.html', context)


def create_travel_post(request):
    form = TravelPostForm(request.POST or None, request.FILES or None)  # request.FILES needed to process images
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'base/travel_post_form.html', context)


def update_travel_post(request, pk):
    obj = get_object_or_404(TravelPost, pk=pk)
    form = TravelPostForm(request.FILES or None, instance=obj)
    if request.method == 'POST':
        print(request.POST)
        form = TravelPostForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            new_travel_post = form.save(commit=False)
            # if request.POST.get('new_tags'):
            #     new_tags = request.POST.get('new_tags')
            #     new_tags = [d.strip() for d in new_tags.split('#')][1:]
            #     print(f'new tags {new_tags}')
            #     for t in new_tags:
            #         t = '#' + t
            #         new_tag = Tag.objects.create(name=t)
            #         new_travel_post.tags.add(new_tag)
            new_travel_post.save()
            form.save_m2m()     #used to save the multiple choice field - CHECK!!!
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'base/travel_post_form.html', context)


def delete_travel_post(request, pk):
    obj = get_object_or_404(TravelPost, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    context = {'obj': obj}
    return render(request, 'base/delete_template.html', context)


def contact(request):
    if request.method == 'POST':
        print(request.POST.get('firstname'))
    return render(request, 'contact.html')