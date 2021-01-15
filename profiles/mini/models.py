from django.db import models

# Create your models here.

class Profile(models.Model):
    DEVELOPER = 'WD' 
    BACKEND = 'BD'
    FRONTEND = 'FD' 
    SENIOR = 'SD'
    DESIGNER = 'DS'
    positions = [   (DEVELOPER, 'Web'),
                    (BACKEND, 'Backend'),
                    (FRONTEND, 'Frontend'),
                    (SENIOR, 'Senior'),
                    (DESIGNER, 'Designer'), 
               ]
    firname = models.CharField(max_length=20)
    lasname = models.CharField(max_length=20)
    positioner = models.CharField( max_length=2,choices=positions)
    
    
    
    def __str__(self):
        return self.firname  +  ' ' +  self.positioner
    