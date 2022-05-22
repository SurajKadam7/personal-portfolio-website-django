"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# this stuff I am additing to see my images data in database using url (extra)
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('blogs/', include('blogs.urls')),             # this link will direct urls to blog app and other process with url happen from there this is relly cool if some one enter blog related url then we simly go in blog app url it just make stuff more organize.
]

# this is for show images in database using url (extra)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# to see how I have added this new urlpatterns just google django media images


