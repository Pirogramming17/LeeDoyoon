from django.shortcuts import render, redirect
from .models import Post
from re import template

# Create your views here.
def review_list(request):
  posts = Post.objects.all()
  context = {'posts': posts}
  print(posts)
  return render(request, template_name="posts/review_list.html", context=context)

def create(request):
  if request.method == 'POST':
    title = request.POST['title']
    date = request.POST['date']
    genre = request.POST['genre']
    score = request.POST['score']
    runningtime = request.POST['runningtime']
    reviewcontent = request.POST['reviewcontent']
    director = request.POST['director']
    actors = request.POST['actors']
    Post.objects.create(title=title, date=date, genre=genre, score=score, runningtime=runningtime, reviewcontent=reviewcontent, director=director, actors=actors)
    return redirect("/") #제출한 내용을 바로 볼 수 있도록 리턴
  else:
    context = {}
    return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
  post = Post.objects.get(id=id)
  context = {
    "post": post
  }
  return render(request, template_name="posts/detail.html", context=context)

def update(request, id):
  if request.method == 'POST':
    title = request.POST['title']
    date = request.POST['date']
    genre = request.POST['genre']
    score = request.POST['score']
    runningtime = request.POST['runningtime']
    reviewcontent = request.POST['reviewcontent']
    director = request.POST['director']
    actors = request.POST['actors']
    Post.objects.filter(id=id).update(title=title, date=date, genre=genre, score=score, runningtime=runningtime, reviewcontent=reviewcontent, director=director, actors=actors)
    return redirect(f"/detail/{id}")
  
  post = Post.objects.get(id=id)
  context = {
    "post":post
  }
  return render(request, template_name="posts/update.html", context=context)

def delete(request,id):
  if request.method == 'POST':
    Post.objects.filter(id=id).delete()
    return redirect("/")