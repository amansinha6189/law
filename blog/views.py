from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from blog.models import Post, BlogComment
# Create your views here.

def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "blog.html", context)
    
def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post)
    context = {"post":post,
                "comments":comments,
                "user": request.user,
                }
                
    return render(request, "blog-single.html", context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno = postSno)
        # parentSno = request.POST.get(sno = parentSno)

        # if parentSno == "":
        #     comment =BlogComment(comment = comment, user = user, post = post)
        # else:
        #     parent = BlogComment.objects.get(sno = parentSno)
        comment =BlogComment(comment = comment, user = user, post = post)
        
        comment.save()
        

    return redirect(f"/blog/{post.slug}")