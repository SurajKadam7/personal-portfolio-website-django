from django.shortcuts import render, get_object_or_404

# importing all the data from the database in which I have created this blog database
from .models import Blog



def all_blog(request):
    # inseted of all I have use orrder_by to order the blog by most recent first
    all_blogs_data = Blog.objects.order_by('-date_of_bloag_post')

    return render(request, 'blogs/home.html', {'all_blogs_data' : all_blogs_data})


def blog_detail(request, blog_id):
    # if primay key pk not exist for blog_id in database then I return 404 server not found error
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogs/details.html', {'blog' : blog})
