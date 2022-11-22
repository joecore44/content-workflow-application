from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Staff, Client, Post
from .models import CompanyProfile, CompanyFollowers
from .models import PostComment, PostRevision
from .forms import StaffRegisterForm, CompanyProfileForm
from .forms import PostCreateForm, PostCommentForm, PostRevisionForm
from django.contrib.auth.decorators import login_required



@login_required
def staff_home(request):
    clients = CompanyProfile.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, './content/staff-index2.html', context)


@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save()
            company.save()
            return redirect('dashboard')
    else:
        form = CompanyProfileForm()
    return render(request, './content/staff-company-create.html', {'form': form})

@login_required
def company_update(request, slug):
    company = CompanyProfile.objects.get(slug=slug)
    form = CompanyProfileForm(instance=company)
    posts = Post.objects.filter(client=company).order_by('-deadline')[:3]
    followers = CompanyFollowers.objects.filter(company=company)
    is_following = CompanyFollowers.objects.filter(user=request.user, company=company).exists()
    

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES, instance=company)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'company': company,
        'posts': posts,
        'followers': followers,
        'is_following': is_following,
        }
    return render(request, './content/staff-company-edit2.html', context)

@login_required
def follow_company(request, slug):
    company = CompanyProfile.objects.get(slug=slug)
    if CompanyFollowers.objects.filter(user=request.user, company=company).exists():
        CompanyFollowers.objects.filter(user=request.user, company=company).delete()
    else:
        CompanyFollowers.objects.create(user=request.user, company=company)
    
    return redirect('update-company', slug=slug)

@login_required
def company_delete(request, slug):
    company = CompanyProfile.objects.get(slug=slug)
    company.delete()
    messages.success(request, f'{company} Successfully Deleted!')
    return redirect('dashboard')

@login_required
def get_company_posts(request, slug):
    company = CompanyProfile.objects.get(slug=slug)
    company_posts = company.post_set.all()
    context = {
        'company': company,
        'posts': company_posts,
    }
    return render(request, './content/staff-company-posts2.html', context)

@login_required
def get_company_post_detail(request, slug, image=None):
    post = Post.objects.get(slug=slug)
    form = PostCreateForm(instance=post)
    revisions_count = PostRevision.objects.filter(post=post).count()

    comment_form = PostCommentForm()
    revision_form = PostRevisionForm()
    if image == None:
        image = 1
    if request.method == 'POST':
        comment_form = PostCommentForm(request.POST)
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        revision_form = PostRevisionForm(request.POST)
        if form.is_valid() and revision_form.is_valid():
            #comment = comment_form.save(commit=False)
            #comment.post = post
            #comment.user = request.user
            #comment.image = image
            #comment.save()
            revision = revision_form.save(commit=False)
            revision.post = post
            revision.staff = request.user.staff
            revision.image = image
            revision.save()
            form.save()
            messages.success(request, f'Account Updated!')
    comments = post.postcomment_set.filter(image=image)
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'form': form,
        'revision_form': revision_form,
        'revisions_count': revisions_count,
        'img': image,
    }
    return render(request, './content/staff-company-post-detail2.html', context)

@login_required
def post_update(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostCreateForm(instance=post)

    if request.method == 'POST':
        print(request)
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        revision_form = PostRevisionForm(request.POST, instance=post)
        if form.is_valid():
            revision_form.post = post
            revision_form.staff = request.user.staff
            print(revision_form)
            revision_form.save()
            form.save()
            messages.success(request, f'Account Updated!')
            return redirect('company-posts', slug=post.client.slug)
    context = {
        'form': form,
        'revision_form': revision_form,
        'post': post,
    }
    return render(request, './content/staff-company-post-create2.html', context)

@login_required
def create_post(request, slug):
    company = CompanyProfile.objects.get(slug=slug)
    posts = Post.objects.filter(client=company).order_by('-deadline')[:3]
    form = PostCreateForm()
    staff = Staff.objects.get(user=request.user)
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.client = company
            post.staff = staff
            post.save(0)
            CompanyFollowers.objects.create(user=request.user, company=company)
            messages.success(request, f'{post.title} Created!')
            return redirect('company-posts', slug=slug)
        else:
            print(form.errors)

    context = {
        'form': form,
        'company': company,
        'posts': posts 
        }
    return render(request, './content/staff-company-post-create2.html', context)

@login_required
def post_timeline(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.postcomment_set.all()
    revisions = post.postrevision_set.all()
   
    context = {
        'post': post,
        'comments': comments,
        'revisions': revisions,
    }
    return render(request, './content/staff-company-post-timeline.html', context)

