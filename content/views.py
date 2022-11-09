from django.shortcuts import render
from django.http import HttpResponse

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

def client_home(request):
    context = {
        'posts': posts
    }
    return render(request, './content/client-index.html', context)

def client_post_detail(request):
    context = {
        'posts': posts,
        'comments': comments
    }
    return render(request, './content/client-post-detail-fb-image.html', context)

