from django.shortcuts import render,redirect,HttpResponseRedirect

# imports of built-in django user model and auth method
from django.contrib.auth.models import User,auth

from django.contrib.auth import logout as auth_logout

# relative imports of forms (manually created models and forms for manual validations and all)
from .models import Posts
from .forms import PostsForm

# import of built-in django messages method from django.contrib for error messages
from django.contrib import messages

# Create your views here.





# register API using django powered Users model
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username = username).exists():
            messages.info(request, 'username already exists!')
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'email already exists!')
            return redirect('register')
        else:
            user = User.objects.create_user(username = username, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')
# login API using django powered authentication
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            # print("login success")
            # messages.info(request, "login success")
            return redirect('index')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')        
    return render(request, 'login.html')

# index page means user page API after login page
def index(request):
    context = {}
    if request.method == "POST":
        # if User.is_authenticated and User.is_active:
        form = PostsForm(request.POST or None)
        if form.is_valid():
            form.save()
            context['form'] = form
            return redirect('posts')
        else:
            form = PostsForm()
    # elif request.method == 'GET':
    #     logout(request)
    #     return redirect('register')
        
        # logout(request)
        # return redirect('register')
        # return render(request, "index.html")
    return render(request, 'index.html', context)

# error page API if post the post without login
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return HttpResponseRedirect('/')
    return render(request,'logout.html')
# posts API for creating the posts
def posts(request):
    # dictionary for initial data with
    # field names as key
    # if request.method == "GET":
    #     logout(request)
    #     return redirect('register')
    context = {}
    # add the dictionary during initialization
    context['dataset'] = Posts.objects.all()
    return render(request, 'posts.html', context)
    