from django.shortcuts import render
from .models import Post
from django.utils import timezone
def announcements(request):
	posts = Post.objects.filter(date__lte=timezone.now()).order_by('-date')
	return render(request, 'announcements/blog.html',{'posts':posts})
def post(request,id):
	post = Post.objects.get(pk=id)
	return render(request, 'announcements/detail.html',{'post':post})