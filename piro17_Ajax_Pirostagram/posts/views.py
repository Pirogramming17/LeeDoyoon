from operator import truediv
from django.shortcuts import render, redirect
from .models import Reply, Post
from .forms import ReplyForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def main(request):
  if request.method=='POST':
    form = ReplyForm(request.POST)
    if form.is_valid():
      form.save()
      redirect( 'posts:main')
  else:
    post = Post.objects.get(id=1)
    reply = Reply.objects.all()
    context = { 
      'replies': reply ,
      'post': post,
    }
    return render(request, template_name='posts/main.html', context=context)
    
  post = Post.objects.get(id=1)
  reply = Reply.objects.all()
  context = { 
    'replies': reply ,
    'post': post,
  }
  return render(request, template_name='posts/main.html', context=context)


@csrf_exempt
def like_post(request):
  req=json.loads(request.body)
  post_id = req['id']
  post = Post.objects.get(id=post_id)

  if post.like == False: 
    post.like = True
  else:
    post.like = False
  post.save()
  return JsonResponse({'id': post.id})

@csrf_exempt
def like_reply(request):
  req=json.loads(request.body)
  reply_id = req['id']
  reply = Reply.objects.get(id=reply_id)

  if reply.like == False: 
    reply.like = True
  else:
    reply.like = False
  reply.save()
  return JsonResponse({'id': reply.id})


@csrf_exempt
def add_reply(request):
  req=json.loads(request.body)
  reply_content = req['content']
  Reply.objects.create(content = reply_content)
  id = Reply.objects.latest('id').id
  reply.save()
  return JsonResponse({'content': reply_content, 'id':id})

@csrf_exempt
def delete_reply(request):
  req=json.loads(request.body)
  del_id = req['id']
  Reply.objects.filter(id=del_id).delete()
  return JsonResponse({'id':del_id})