# I have made this urls.py and the stuff inside it (extra)
from django.urls import path
from . import views   # I have use just . because urls.py and views are on same level

# this is used in home.html to show that blog_details is memeber of blogs class in the project there are so many applications which is having same name in path so to uderstand django that which name is of which app url we use app name
app_name = 'blogs'

urlpatterns = [
    path('', views.all_blog, name = 'all_blog'),

    # http://127.0.0.1:8000/blogs/any_integer_number    for this type of url below path work we don't need to create path form all numbers due to this
    path('<int:blog_id>/', views.blog_detail, name = 'blog_detail'),  # note we can't use space like <int : blog_id> we can see error in server tailing that don't use space

]

