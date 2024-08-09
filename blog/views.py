from django.shortcuts import render , redirect
from django.http import HttpResponse
from blog.models import BlogModel , BlogComment 
# Create your views here.

def blogHome(request):
       
       allBlogPost = BlogModel.objects.all()
       context = {
              "allBlogPost" : allBlogPost
       }
       
       
       return render(request, "blog/bloghome.html" , context)

def blogPost(request , name):
       
       singleBlogPost = BlogModel.objects.filter( slug=name).first()
       singlepostcomment = BlogComment.objects.filter(post=singleBlogPost)
       context = {
              "singleBlogPost" : singleBlogPost , "allcomment" : singlepostcomment
       }
     
               
       return render(request , "blog/blogpost.html" , context)

def blogComment(request):
      
          
       if request.method == "POST":  

          comment = request.POST.get("comment")
          singleblogpostsno = request.POST.get("blogpostsno")
          user = request.user
          singleblogpost = BlogModel.objects.get(sno=singleblogpostsno)
          parentsno = request.POST.get("parentsno")
          if parentsno == "":
              Blog_save =  BlogComment(comment = comment , user = user , post=singleblogpost)
              Blog_save.save()
              return redirect('/blog')
          else:
              parent = BlogComment.objects.get(sno=parentsno)
              print(parent , " parent ho gya hy ")
              Blog =  BlogComment(comment = comment , user = user , post=singleblogpost , parent=parent)
              b =  Blog.save()
              print(b)
              return redirect('/blog')
       
       
       return HttpResponse("kuch masla hy")
       
      