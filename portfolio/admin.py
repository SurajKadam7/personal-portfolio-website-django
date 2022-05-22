from django.contrib import admin

from .models import Project

# here we making connection with our database and we can now see all the models in our database by using below command.
admin.site.register(Project)

