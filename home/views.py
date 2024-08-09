from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login , logout as auth_logout , authenticate
from .models import ContactModel
from blog.models import BlogModel
# Create your views here.

def home(request):
    return render(request , "home/home.html")

def about(request):
    return render(request , "home/about.html")

def contact(request):
 
        
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        complain = request.POST['complain']
        contact_data = ContactModel(name = name , email = email , phone = phone , complain = complain)
        print('data base hpo gya')
        contact_data.save()
  
    return render(request , "home/contact.html")
   

def search(request):
    
    querry = request.GET["search"]
    SearchBlogPost = BlogModel.objects.filter(title__icontains=querry)
    params = {"SearchBlogPost" : SearchBlogPost}
    
    for s in SearchBlogPost :
        print(s.title)
        
    return render(request , "home/search.html" , params )

def signin(request):
   
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        
        if not username:
            return redirect('/')
        
        db_user = User.objects.create_user(username , email , password)
        db_user.first_name = fname
        db_user.last_name = lname
        db_user.save()
        
    return  redirect('/')    
    
def login(request):
    
    username = request.POST["username"]
    password = request.POST["password"]
    
    print(username , password)
   
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        auth_login( request , user)
        return redirect('/')
    else:
        print("user nhi mila")
        
    return redirect('/')      
    
    
   
    
def logout(request):
     
     logout_user = auth_logout(request)
     print(logout_user)
     print("user is logout succesfully")
     
     return redirect('/')
     