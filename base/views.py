from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TravelPost, Tag, Comment, Like
from .forms import TravelPostForm, CommentForm
from travelblog.settings import MEDIA_ROOT, MEDIA_URL


#not a view func
def add_tags(rq, tp):
    if rq.POST.get('new_tags'):
        new_tags = rq.POST.get('new_tags')
        new_tags = (d.strip() for d in new_tags.split('#'))
        next(new_tags)  # first record is a garbage, omit it
        for t in new_tags:
            t = '#' + t.replace(' ', '_').capitalize()
            all_tags = (tg.name for tg in Tag.objects.all())
            if t not in all_tags:
                tag = Tag.objects.create(name=t)
            else:
                tag = Tag.objects.get(name=t)
                print('HERE ', tag)
            tp.tags.add(tag)


def home(request, *args, **kwargs):
    posts_per_page = 3
    travel_posts_all = None
    travel_post_newest = None
    travel_posts_1 = None
    travel_posts_2 = None
    no_posts = True
    one_page_available = False
    two_page_available = False


    travel_posts_all = TravelPost.objects.all()
    posts_number = len(travel_posts_all)
    if posts_number:
        no_posts = False
        travel_post_newest = travel_posts_all.first()
        if posts_number > 1 and posts_number <= posts_per_page + 1:
            one_page_available = True
            travel_posts_1 = travel_posts_all[1:posts_per_page+1]
        elif posts_number > posts_per_page + 1:
            two_page_available = True
            travel_posts_1 = travel_posts_all[1:posts_per_page+1]
            travel_posts_2 = travel_posts_all[posts_per_page+1:posts_per_page*2+1]

    context = {
        'travel_post_newest':travel_post_newest,
        'travel_posts_1':travel_posts_1,
        'travel_posts_2':travel_posts_2,
        'no_posts': no_posts,
        'one_page_available': one_page_available,
        'two_page_available': two_page_available
    }
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)


def travel_post(request, pk):
    travel_post = get_object_or_404(TravelPost, pk=pk)
    # tags = travel_post.tags.all()                     # accessing many to many relation classes, done on the template side
    new_comment = None

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = travel_post
            new_comment.author = request.user
            new_comment.save()
            return redirect('travel-post', pk=travel_post.pk)

    context = {
        'travel_post': travel_post,
        'form': form,
        }
    return render(request, 'base/travel_post.html', context)


@login_required(login_url='/account/login/')
def like(request, pk):
    print("HELLO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    comment = get_object_or_404(Comment, pk=pk)
    comment_likes = comment.likes
    like = Like.objects.filter(author=request.user, comment=comment).count()

    if not like:
        like = Like.objects.create(author=request.user, comment=comment)
        comment_likes = comment_likes + 1
    else:
        like = Like.objects.filter(author=request.user, comment=comment).delete()
        comment_likes = comment_likes - 1
    
    comment.likes = comment_likes
    comment.save()

    return redirect('travel-post', pk=comment.post.id)


@login_required(login_url='/account/login/')
def create_travel_post(request):
    form = TravelPostForm(request.POST or None, request.FILES or None)  # request.FILES needed to process images
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            new_travel_post = form.save()
            add_tags(request, new_travel_post)
            new_travel_post.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'base/travel_post_form.html', context)

@login_required(login_url='/account/login/')
def update_travel_post(request, pk):
    obj = get_object_or_404(TravelPost, pk=pk)
    form = TravelPostForm(request.FILES or None, instance=obj)
    if request.method == 'POST':
        form = TravelPostForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            updated_travel_post = form.save(commit=False)           
            form.save_m2m()      # needed to save existing checked/unchecked tags
            add_tags(request, updated_travel_post)  # needed to create new tags and add them to the travel post
            updated_travel_post.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'base/travel_post_form.html', context)

@login_required(login_url='/account/login/')
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