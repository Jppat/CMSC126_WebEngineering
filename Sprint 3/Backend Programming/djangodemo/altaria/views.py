from django.shortcuts import render
from .models import Post
# Create your views here.
def view_article(request):
	post_object = Post.objects.first()
	context = {
	'post_object': post_object
	}
	return render(request, "posts/index.html", context)

# def index(request)