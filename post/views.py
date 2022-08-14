
from xml.etree.ElementTree import Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from post.models import Stream, Post, Tag, Likes, PostFileContent
from post.forms import NewPostForm
#from stories.models import Story, StoryStream
#from comment.models import Comment
#from comment.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from authy.models import Profile


@login_required
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    #stories = StoryStream.objects.filter(user=user)
    group_ids = []
    for post in posts:
        group_ids.append(post.post_id)
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    template = loader.get_template('index.html')
    context = {
        'post_items': ,
        'post_items': stories,
    }