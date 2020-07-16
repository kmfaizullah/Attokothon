from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login, name='login'), # this url i for user login
    path('signup', views.signup, name='signup'), # this is for user signup
    path('home', views.home, name='home'), # this is home page url
    path('bestPlace', views.bestPlaces, name='bestPlace'), # this is best place page url
    path('blog', views.blogs, name='blog'), # this is blog page url
    path('memorable', views.memorable, name='memorable'), # this is memorable page url
    path('todo', views.todos, name='todo'), # this is todo page url
    path('todo_form', views.todo_form, name='todo_form'), # this is todo form page url
    path('bplace_form', views.bplace_form, name='bplace_form'), # this is todo form page url
    path('blog_form', views.blog_form, name='blog_form'), # this is todo form page url
    path('memorable_form', views.memorable_form, name='memorable_form'), # this is todo form page url
    path('blog_delete/<int:id>/', views.blog_delete,name='blog_delete'),
    path('<int:id>', views.blog_form,name ='blog_update'),
    path('place_delete/<int:id>/', views.place_delete,name='place_delete'),
    path('place_update/<int:id>/', views.bplace_form,name ='place_update'),
    path('memory_delete/<int:id>/', views.memory_delete,name='memory_delete'),
    path('memory_update/<int:id>/', views.memorable_form,name ='memory_update'),
    path('todo_delete/<int:id>/', views.todo_delete,name='todo_delete'),
    path('todo_update/<int:id>/', views.todo_form,name ='todo_update'),

]