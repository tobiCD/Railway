from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .filter import *
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .models import *
def home(request):
    posts = Post.objects.filter()[0:5]
    context = {'posts': posts}
    return render(request ,'index.html',context)

def posts(request):
	posts = Post.objects.filter(active=True)
	myFilter = Postfilter(request.GET, queryset=posts)
	posts = myFilter.qs

	page = request.GET.get('page')

	paginator = Paginator(posts, 3)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts':posts, 'myFilter':myFilter}
	return render(request, 'posts.html', context)


def POST(request,slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'Post.html', context)
def profile(request):
    return render(request,'profile.html')




#CRUD views

def create_Post(request):
    form = PostForm()
    if request.method =="POST":
        form =PostForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
        else:
            messages.error(request,"form is not valid ")
        return redirect('posts')
    context = {'form':form}
    return render(request, 'post_form.html', context)


def update_Post(request,slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method =="POST":
        form =PostForm(request.POST, request.FILES ,instance=post)
        if form.is_valid:
            form.save()
        return redirect('post' , post.slug)
    context = {'form':form}
    return render(request, 'post_form.html', context)

def delete_Post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context={"item":post}
    return render(request ,'delete.html',context)


def send_email(request):
    if request.method =='POST':
        template_name = render_to_string('send_email_template.html',{
            'name':request.POST['name'],
             'email':request.POST['email'],
            'message':request.POST['message']
        })
        email = EmailMessage(
            request.POST['subject'],
            template_name,
            settings.EMAIL_HOST_USER,
            ['khoichudang1@gmail.com'],
       )
        email.send()
    return render(request,'email_sent.html')


def LoginView(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password=password)       
      
        if user is not None:
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
             messages.error(request , 'username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def Logout(request):
     logout(request)
     return render(request,'logout.html')
def Register(request):
    form = RegistrationForm()
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request,"account successfully created ")
            user = authenticate(request, email=user.email , password=request.POST['password1'])
            login(request , user )
            redirect('login')
        else:
            messages.error(request,'An error has occured with registration')
    context = {'form': form}
    return render(request, 'register.html',context)
                    
        
def Todolist(request):
    return render(request, 'list.html')