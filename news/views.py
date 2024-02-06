from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView

from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles

    form_class = ArticlesForm

    template_name = 'news/create.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма неверно заполнена'
    else:
        form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create.html', data)
