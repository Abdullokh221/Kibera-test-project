from django.shortcuts import render, redirect
from .models import New
from .forms import NewsForm
from django.core.paginator import Paginator



# Create your views here.
def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    news = New.objects.filter(title__icontains=q).order_by('date_uploaded')[::-1]
    
    
    page_num = request.GET.get('page', 1)
    paginator = Paginator(news, 10)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        
        page_obj = paginator.page(1)
    except EmptyPage:
        
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'news': news,
        'page_obj': page_obj,
    }
    return render(request, 'news/index.html', context)

def create(request):
    news = New.objects.order_by('date_uploaded')[::-1]
    context = {'news': news}
    form = NewsForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    render(request, 'news/index.html', context)
    return redirect('index')


def edit(request, id):
    news = New.objects.get(id=id)
    form = NewsForm(instance=news)

    context = {'form': form, 'news': news}
    return render(request, 'news/edit.html', context)

def update(request, id):
    title = request.POST.get('title')
    description = request.POST.get('description')
    author = request.POST.get('author')
    news = New.objects.get(id=id)
    news.title = title
    news.description = description
    news.author = author
    news.save()
    return redirect(index)

def delete(request, id):
    news = New.objects.get(id=id)
    news.delete()
    return redirect(index)

