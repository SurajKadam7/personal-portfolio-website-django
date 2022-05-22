from django.db import models

class Project(models.Model):

    tital = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)               # blank will make the url optional if we wan't we add it else not blank can be apply to any of the above

# by usign below code in our admine pannel we can add the name of the tital insted of default name project1 porject
    def __str__(self):
        return self.tital
    
# Create your models here.
