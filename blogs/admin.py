from django.contrib import admin

from .models import Blog

# do add blogs in our database we created it (extra)
admin.site.register(Blog)
