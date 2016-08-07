from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import PostForm
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
    # if request.method == "POST":
    #     content = request.POST.get("content")
    #     title = request.POST.get("title")
    #     Post.objects.create(title=title,content=content)
    context = {
        "form" : form,
    }
    return render(request, "post_form.html", context)
    # return HttpResponse("<h1>Create </h1>")

def post_detail(request,id=None):
    #instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post,id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List"
    }
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }
    return render(request, "post_list.html", context)

def post_update(request):

    return HttpResponse("<h1>Update </h1>")

def post_delete(request):

    return HttpResponse("<h1>Delete </h1>")
