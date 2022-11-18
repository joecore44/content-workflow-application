from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Staff, Client, Post
from .models import CompanyProfile, CompanyFollowers, PostComment
from .forms import StaffRegisterForm, CompanyProfileForm
from .forms import PostCreateForm, PostCommentForm
from django.contrib.auth.decorators import login_required

posts = [
    {
        'id': 1,
        'author': 'Joe Shepard',
        'type': 'Facebook Image',
        'title': 'Facebook Post 1',
        'content': 'How is a Visual Identity Different from a Brand Identity & Why It Matters to Your Brand What is Visual Identity?',
        'image': 'https://dev.graylingagency.co/sites/grayling-v2/wp-content/uploads/2022/11/visual-identity-differ-from-brand-identity.png',
        'date_posted': 'November 09, 2022',
        'date_approval': 'November 14, 2022',
        'status': 'Pending Customer Approval',
    },
    {
        'id': 2,
        'author': 'Joe Shepard',
        'type': 'Facebook Video',
        'title': 'Instagram Post 1',
        'content': 'Second post content',
        'image': 'https://dev.graylingagency.co/sites/grayling-v2/wp-content/uploads/2022/11/visual-identity-differ-from-brand-identity.png',
        'date_posted': 'November 09, 2022',
        'date_approval': 'November 14, 2022',
        'status': 'Pending Customer Approval',
    }
    ,
    {
        'id': 3,
        'author': 'Cutter Streeby',
        'type': 'Facebook Image',
        'title': 'Instagram Post 2',
        'content': '2nd post content',
        'image': 'https://dev.graylingagency.co/sites/grayling-v2/wp-content/uploads/2022/11/visual-identity-differ-from-brand-identity.png',
        'date_posted': 'November 09, 2022',
        'date_approval': 'November 21, 2022',
        'status': 'Pending Customer Approval',
    },
    {
        'id': 4,
        'author': 'Joe Shepard',
        'type': 'Instagram Story',
        'title': 'Linkedin Post 1',
        'content': '1st Linkedin post content',
        'image': 'https://dev.graylingagency.co/sites/grayling-v2/wp-content/uploads/2022/11/visual-identity-differ-from-brand-identity.png',
        'date_posted': 'November 09, 2022',
        'date_approval': 'November 23, 2022',
        'status': 'Pending Customer Approval',
    },
    {
        'id': 5,
        'author': 'Joe Shepard',
        'type': 'Facebook Image',
        'title': 'Twitter Post 1',
        'content': '1st Twitter post content',
        'image': 'https://startbootstrap.github.io/startbootstrap-sb-admin-2/img/undraw_posting_photo.svg',
        'date_posted': 'November 09, 2022',
        'date_approval': 'November 25, 2022',
        'status': 'Pending Customer Approval',
    }
]

backup_clients = [
    {
        'id': 1,
        'name': 'Joe Shepard',
        'company_name': 'Grayling',
        'email': 'joe@graylingagency.com',
        'phone': '555-555-5555',
        'status': 'Active',
        'number_of_open_posts': '5',
    },
    {
        'id': 2,
        'name': 'Jordann Shepard',
        'company_name': 'Core Nutrition',
        'email': 'jordann@corenutritionpv.com',
        'phone': '555-555-5555',
        'status': 'Active',
        'number_of_open_posts': '10',
    },
    {
        'id': 3,
        'name': 'Jordann Shepard',
        'company_name': 'Core Nutrition',
        'email': 'jordann@corenutritionpv.com',
        'phone': '555-555-5555',
        'status': 'Active',
        'number_of_open_posts': '10',
    },
    {
        'id': 3,
        'name': 'Jordann Shepard',
        'company_name': 'Core Nutrition',
        'email': 'jordann@corenutritionpv.com',
        'phone': '555-555-5555',
        'status': 'Active',
        'number_of_open_posts': '10',
    }
    ,
    {
        'id': 3,
        'name': 'Jordann Shepard',
        'company_name': 'Core Nutrition',
        'email': 'jordann@corenutritionpv.com',
        'phone': '555-555-5555',
        'status': 'Active',
        'number_of_open_posts': '10',
    }
    ,
    {
        'id': 3,
        'name': 'Jordann Shepard',
        'company_name': 'Core Nutrition',
        'email': 'jordann@corenutritionpv.com',
        'phone': '555-555-5555',
        'status': 'Active',
        'number_of_open_posts': '10',
    }
    ,
    {
        'id': 3,
        'name': 'Jordann Shepard',
        'company_name': 'Core Nutrition',
        'email': 'jordann@corenutritionpv.com',
        'phone': '555-555-5555',
        'status': 'Active',
        'number_of_open_posts': '10',
    }
    ,
    {
        'id': 3,
        'name': 'Jordann Shepard',
        'company_name': 'Core Nutrition',
        'email': 'jordann@corenutritionpv.com',
        'phone': '555-555-5555',
        'status': 'Active',
        'number_of_open_posts': '10',
    }
    ,
    {
        'id': 3,
        'name': 'Jordann Shepard',
        'company_name': 'Core Nutrition',
        'email': 'jordann@corenutritionpv.com',
        'phone': '555-555-5555',
        'status': 'Active',
        'number_of_open_posts': '10',
    }
]

comments = [
    {
        'id': 1,
        'post_id': 1,
        'avatar': 'https://personal-portfolio-v2-ae3h.vercel.app/images/formal-image-joe-s.png',
        'author': 'Joe Shepard',
        'content': 'This is a comment',
        'date_posted': '11/09/2022 2:00 PM',
        'status': 'Pending',
    },
    {
        'id': 2,
        'post_id': 1,
        'avatar': 'https://personal-portfolio-v2-ae3h.vercel.app/images/formal-image-joe-s.png',
        'author': 'Joe Shepard',
        'content': 'Can you fix the typo on the 3rd line? Thank you. 👌🏼',
        'date_posted': '11/09/2022 4:00 PM',
        'status': 'Pending',
    }
]

@login_required
def client_home(request):
    context = {
        'posts': posts,
        'comments': comments,
    }
    return render(request, './content/client-index.html', context)

@login_required
def staff_home(request):
    clients = CompanyProfile.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, './content/staff-index2.html', context)

        
@login_required
def client_post_detail(request):
    context = {
        'posts': posts,
        'comments': comments,
    }
    return render(request, './content/staff-post-detail-fb-image.html', context)

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
    comment_form = PostCommentForm()
    if image == None:
        image = 1
    if request.method == 'POST':
        comment_form = PostCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.image = image
            comment.save()
    comments = post.postcomment_set.filter(image=image)
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'img': image,
    }
    return render(request, './content/staff-company-post-detail2.html', context)

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

