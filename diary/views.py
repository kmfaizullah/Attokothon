from django.shortcuts import render, redirect
from .forms import SignupForm, blogForm, bestPlaceForm, memoryForm, todoForm
from .models import Signup,blog,bestPlace,memory, todo
from django.contrib import auth

#from .forms import EmployeeForm
#from .models import Employee

# Create your views here.


def login(request):
    if request.method == 'POST':
        uname = request.POST['user'] 
        passw = request.POST['password']
        
        try :
            sign = Signup.objects.get(user_name = uname, password = passw)
            return redirect("home")

        except:
            return redirect("login")
    
    if request.method == 'GET':
        return render(request, "diary/login.html")



def signup(request, id =0):
    if request.method == "GET":
        if id == 0:
            form = SignupForm()
        else:
            signup = Signup.objects.get(pk=id)
            form = SignupForm(instance=signup)
        return render(request, "diary/signup.html", {'form': form})
    else:
        if id == 0:
            form = SignupForm(request.POST)
        else:
            employee = Signup.objects.get(pk=id)
            form = SignupForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('login')

def home(request):
    return render(request, "diary/home.html")

def bestPlaces(request):
    context = {'place_list': bestPlace.objects.all()}
    return render(request, "diary/bestPlace.html", context)

def blogs(request):
    context = {'blog_list': blog.objects.all()}
    return render(request, "diary/blog.html", context)

def memorable(request):
    context = {'memory_list': memory.objects.all()}
    return render(request, "diary/memorableJourney.html",context)

def todos(request):
    context = {'todo_list': todo.objects.all()}
    return render(request, "diary/todo.html",context)

def bplace_form(request, id =0):

    if request.method == "GET":
        if id == 0:
            form = bestPlaceForm()
        else:
            values = bestPlace.objects.get(pk=id)
            form = bestPlaceForm(instance=values)
        return render(request, "diary/best_place_form.html", {'form': form})
    else:
        if id == 0:
            form = bestPlaceForm(request.POST)
        else:
            values = bestPlace.objects.get(pk=id)
            form = bestPlaceForm(request.POST,instance= values)
        if form.is_valid():
            form.save()
        return redirect('bestPlace')
        

def blog_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = blogForm()
        else:
            values= blog.objects.get(pk=id)
            form = blogForm(instance=values)
        return render(request, "diary/blog_post_form.html", {'form': form})
    else:
        if id == 0:
            form = blogForm(request.POST)
        else:
            values = blog.objects.get(pk=id)
            form = blogForm(request.POST,instance= values)
        if form.is_valid():
            form.save()
        return redirect('blog')

def memorable_form(request, id =0):
    if request.method == "GET":
        if id == 0:
            form = memoryForm()
        else:
            values = memory.objects.get(pk=id)
            form = memoryForm(instance=values)
        return render(request, "diary/memorable_journey_form.html", {'form': form})
    else:
        if id == 0:
            form = memoryForm(request.POST)
        else:
            values = memory.objects.get(pk=id)
            form = memoryForm(request.POST,instance= values)
        if form.is_valid():
            form.save()
        return redirect('memorable')

def todo_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = todoForm()
        else:
            values = todo.objects.get(pk=id)
            form = todoForm(instance=values)
        return render(request, "diary/todo_form.html", {'form': form})
    else:
        if id == 0:
            form = todoForm(request.POST)
        else:
            values = todo.objects.get(pk=id)
            form = todoForm(request.POST,instance= values)
        if form.is_valid():
            form.save()
        return redirect('todo')


def blog_delete(request,id):
     blogs = blog.objects.get(pk=id)
     blogs.delete()
     return redirect('blog')

def place_delete(request,id):
     places = bestPlace.objects.get(pk=id)
     places.delete()
     return redirect('bestPlace')

def memory_delete(request,id):
     memories = memory.objects.get(pk=id)
     memories.delete()
     return redirect('memorable')

def todo_delete(request,id):
     todos = todo.objects.get(pk=id)
     todos.delete()
     return redirect('todo')