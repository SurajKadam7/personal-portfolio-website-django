from django.db import models

# the below class is created by me

class Blog(models.Model):

    blog_tital = models.CharField(max_length=100)
    blog_description = models.TextField()
    date_of_bloag_post = models.DateField()


# by usign below code in our admine pannel we can add the name of the tital insted of default name blg 1 blog2
    def __str__(self):
        return self.blog_tital
    



# important :-    don't forgot to migrate all this models after crating use this command :- python manage.py makemigrations
#                 then use python manage.py migrate and run server
    
