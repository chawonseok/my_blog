from django.shortcuts import render
from .models import Post
from django.urils import timezone

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(
        published_data__lte=timezone.new().order_by('published_date'))
    return render(request, 'blog/post_list.html', {'posts': posts})
