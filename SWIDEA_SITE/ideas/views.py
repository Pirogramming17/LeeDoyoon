from django.shortcuts import render, redirect
from .models import Idea, DevTool

# Create your views here.
def home(request):
  orderby = request.GET.get('orderby', None)
  # 최신순 정렬
  if orderby == 'recent': #상단에 최신에 등록한 글이 올라오도록 정렬
    idea = Idea.objects.all().order_by('-created_at')
  # 등록순 정렬
  elif orderby == 'create': #상단에 가장 먼저 등록한 글이 올라오도록 정렬
    idea = Idea.objects.all().order_by('created_at')
  # 이름순 정렬
  elif orderby == 'name': #알파벳 또는 ㄱㄴㄷ 순으로 위에서 아래로 정렬
    idea = Idea.objects.all().order_by('title')
  # 찜한 아이디어만 정렬
  elif orderby == 'select':
    idea = Idea.objects.all().get(select__exact = True)
  # 관심도순 정렬
  elif orderby == 'interest': #관심도가 높은 것부터 위에서 아래로 정렬
    idea = Idea.objects.all().order_by('-interest')
  else:
    idea = Idea.objects.all()
  context = {
    'idea': idea,
    'orderby': orderby,
  }
  return render(request, template_name='ideas/home.html', context=context)

def idea_create(request):
  devtool = DevTool.objects.all()
  if request.method == 'POST':
    title = request.POST['title']
    image = request.FILES['image']
    content = request.POST['content']
    interest = request.POST['interest']
    devtool = DevTool.objects.get(name = request.POST['devtool'])
    Idea.objects.create(title=title, image=image, content=content, interest=interest, devtool=devtool)
    curid = Idea.objects.last().id
    return redirect(f'/idea_detail/{curid}')
  else:
    context = {'devtool': devtool}
    return render(request, template_name='ideas/idea_create.html', context=context)

def idea_detail(request, id):
  idea = Idea.objects.get(id=id)
  context = {
    'idea': idea,
  }
  return render(request, template_name = 'ideas/idea_detail.html', context=context)

def idea_update(request, id):
  devtool = DevTool.objects.all()
  if request.method == 'POST':
    title = request.POST['title']
    image = request.FILES['image']
    content = request.POST['content']
    interest = request.POST['interest']
    devtool = DevTool.objects.get(name = request.POST['devtool'])
    Idea.objects.filter(id=id).update(title=title, image=image, content=content, interest=interest, devtool=devtool)
    return redirect(f'/idea_detail/{id}')
  else:
    idea = Idea.objects.get(id=id)
    context = {
      'idea': idea, 
      'devtool':devtool
      }
    return render(request, template_name='ideas/idea_update.html', context=context)
  
def idea_delete(request,id):
  if request.method == 'POST':
    Idea.objects.filter(id=id).delete()
    return redirect('/')

def devtool_list(request):
  devtool = DevTool.objects.all()
  context = {'devtool': devtool}
  return render(request, template_name='ideas/devtool_list.html', context=context)

def devtool_create(request):
  if request.method == 'POST':
    name = request.POST['name']
    kind = request.POST['kind']
    content = request.POST['content']
    DevTool.objects.create(name=name, kind=kind, content=content)
    devid = DevTool.objects.last().id
    return redirect(f'/devtool_detail/{devid}')
  else:
    devtool = DevTool.objects.all()
    context={
      'devtool': devtool
    }
    return render(request, template_name='ideas/devtool_create.html', context=context)

def devtool_detail(request, id):
  devtool = DevTool.objects.get(id=id)
  all_idea = devtool.devtool_list.all()
  context = {
    'devtool': devtool,
    'all_idea':all_idea,
  }
  return render(request, template_name='ideas/devtool_detail.html', context=context)

def devtool_update(request, id):
  if request.method == 'POST':
    name = request.POST['name']
    kind = request.POST['kind']
    content = request.POST['content']
    DevTool.objects.filter(id=id).update(name=name, kind=kind, content=content)
    return redirect(f'/devtool_detail/{id}')
  
  devtool = DevTool.objects.get(id=id)
  context = { 'devtool':devtool}
  return render(request, template_name='ideas/devtool_update.html', context=context)

def devtool_delete(request,id):
  if request.method=='POST':
    DevTool.objects.filter(id=id).delete()
    return redirect('/devtool_list')