from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.models import User
from .froms import PostForm

# Create your views here.
# def post_list(request):
#     posts = Post.objects.filter(status = 'pub')
#     context = {'posts': posts}
#     return render(request,"blog/post.html", context)
class PostListView(generic.ListView):
    template_name = 'blog/post.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(status = 'pub')

# def post_deatail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     context = {'post': post}
#
#     return render(request, "blog/post_det.html", context)
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_det.html'
    context_object_name = 'post'
# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostForm()
#     return render(request,"blog/creat_post.html", {'form':form})
class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/creat_post.html'

# def post_update(request, pk):
#     post = get_object_or_404(Post,pk=pk)
#     form = PostForm(request.POST or None ,instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#     return render(request,'blog/creat_post.html',{'form':form})
class PostUpdateView(generic.UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'blog/creat_post.html'
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         return redirect('post_list')
#     return render(request,'blog/post_delete.html',context = {"post":post})
#
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
