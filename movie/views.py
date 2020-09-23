from django.shortcuts import render, redirect
from .models import News
from .forms import NewsCreate
from django.http import HttpResponse


def index(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})


def upload(request):
    upload = NewsCreate()
    if request.method == 'POST':
        upload = NewsCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'news/upload_form.html', {'upload_form':upload})


def update_news(request, news_id):
    news_id = int(news_id)
    try:
        new_sel = News.objects.get(id = news_id)
    except News.DoesNotExist:
        return redirect('index')
    new_form = NewsCreate(request.POST or None, instance = new_sel)
    if new_form.is_valid():
       new_form.save()
       return redirect('index')
    return render(request, 'news/upload_form.html', {'upload_form':new_form})


def delete_news(request, news_id):
    news_id = int(news_id)
    try:
        new_sel = News.objects.get(id = news_id)
    except News.DoesNotExist:
        return redirect('index')
    new_sel.delete()
    return redirect('index')