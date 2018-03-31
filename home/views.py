from django.shortcuts import render
from announcements.models import Post
from django.utils import timezone
def home(request):
	posts = Post.objects.filter(date__lte=timezone.now()).order_by('-date')[:3]
	return render(request, 'home/home.html', {'posts': posts})