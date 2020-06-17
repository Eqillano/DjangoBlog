from django.shortcuts import render
from django.views.generic import ListView,DetailView

# Create your views here.
from django.http import HttpResponse
from .models import Post,Category,Tag


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2


    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


class PostByCategory(ListView):
    model =
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 1
    all_empty = False


    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])


    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

class PostDetail(DetailView):
    model = Post


def index(request):
    template = 'blog/index.html'
    context = {}
    return render(request,template,context)

def get_category(request,slug):
    return render(request,'blog/category.html')
