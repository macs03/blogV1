from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import PostForm
from .models import Post

def post_create(request):
    if not request.user.is_staff or not  request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        # print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "Creado exitosamente")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"No se ha creado el post")
    # if request.method == "POST":
    #     content = request.POST.get("content")
    #     title = request.POST.get("title")
    #     Post.objects.create(title=title,content=content)
    context = {
        "form" : form,
        "action": "Create",
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

    query = request.GET.get("q")

    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)
        ).distinct()

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

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        # print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "Modificado exitosamente")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "No se ha Modificado el post")
    context = {
        "title": instance.title,
        "instance": instance,
        "action": "Edit",
        "form": form
    }
    return render(request, "post_form.html",context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Borrado exitosamente")
    return redirect("posts:postList")
