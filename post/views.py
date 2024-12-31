from django.shortcuts import render,redirect
from .models import Post, Like
from .forms import *
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    posts = Post.objects.all()  # Getting all the posts from database
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
    return render(request, 'post/index.html', { 'posts': posts,'form': form })

def post_detail(request, p_id):
    post = Post.objects.get(pk=p_id)  
    return render(request, 'post/details.html', {'post': post})

def post_posts(request):
    posts = Post.objects.all()  # Getting all the posts from database
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return JsonResponse({'success': True, 'post': {'id': post.id, 'post_heading': post.post_heading}})
        else:
        # Convert form errors to a serializable format
            errors = {field: error.get_json_data() for field, error in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)

def getPosts(request):
    posts = Post.objects.all()  # Getting all the posts from database
    return JsonResponse({'posts':list(posts.values())}, safe=False)

def likePost(request):
    if request.method == 'GET':
           post_id = request.GET['post_id']
           likedpost = Post.objects.get(pk=post_id) #getting the liked posts
           m = Like(post=likedpost) # Creating Like Object
           m.save()  # saving it to store in database
           return HttpResponse("Success!") # Sending an success response
    else:
           return HttpResponse("Request method is not a GET")
    
def delete(request, p_id):
    if request.method == 'GET':
        post = Post.objects.get(pk=p_id)
        post.delete()
        return redirect('index')