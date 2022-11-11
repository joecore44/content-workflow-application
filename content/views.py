from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ClientRegisterForm, StaffRegisterForm, ClientUpdateForm, ClientUpdateProfileForm
from django.http import HttpResponse
from .models import Staff, Client, Post
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

clients = [
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
    if Staff.objects.filter(user=request.user).exists():
        if request.method == 'POST':
            form = ClientUpdateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                messages = 'Account created for ' + request.POST['company_name']
                return redirect('dashboard')
        else:
            form = ClientUpdateProfileForm()
            context = {
                'clients': clients,
                'form': form
            }
            return render(request, './content/staff-index.html', context)

        
@login_required
def client_post_detail(request):
    context = {
        'posts': posts,
        'comments': comments
    }
    return render(request, './content/client-post-detail-fb-image.html', context)

@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-profile', pk=pk)
    else:
        form = ClientRegisterForm()
    return render(request, './content/staff-add-client.html', {'form': form})



@login_required
def client_profile(request, pk):
    user = User.objects.get(id=pk)
    print(user.username)
    if request.method == 'POST':
        cu_form = ClientUpdateForm(request.POST,
             instance=user)
        cp_form = ClientUpdateProfileForm(request.POST,
            instance=user)
        if cu_form.is_valid() and cp_form.is_valid():
            cu_form.save()
            cp_form.save()
            messages.success(request, f'Client account has been updated!')
            return redirect('client-profile', pk=pk)
    else:
        cu_form = ClientUpdateForm(instance=user)
        cp_form = ClientUpdateProfileForm(instance=user, initial={'user': user})
    context = {
        'cu_form': cu_form,
        'cp_form': cp_form
    }

    return render(request, './content/staff-manage-client.html', context)

