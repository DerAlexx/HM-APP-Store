from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField,ArrayField
from django.utils import timezone
#from users.models import CustomUser

'''
creating the directory depending on the username 
and the file to store it
'''
def user_directory_path(instance, filename):
      return 'user_{0}/{1}'.format(instance.creator.getUserName(), filename)

'''
Model for APPs
'''
class APP(models.Model):
    TypeOfUserAccount = (
    ('ST', 'Student'), #student
    ('SA', 'Staff'), #staff
    ('PR', 'Professor'), #Prof
    ('Fr', 'Externer Student'), #foreign
    ('All','Non Type') #for Everybody
    )

    FK = (
    ('FK00', 'General'),
    ('FK01', 'Fakultät 01'),  
    ('FK02', 'Fakultät 02'),  
    ('FK03', 'Fakultät 03'),  
    ('FK04', 'Fakultät 04'),  
    ('FK05', 'Fakultät 05'),  
    ('FK06', 'Fakultät 06'),  
    ('FK07', 'Fakultät 07'),  
    ('FK08', 'Fakultät 08'),  
    ('FK09', 'Fakultät 09'),  
    ('FK10', 'Fakultät 10'),  
    ('FK11', 'Fakultät 11'),  
    ('FK12', 'Fakultät 12'),  
    ('FK13', 'Fakultät 13'),  
    ('FK14', 'Fakultät 14'),  
    )

    appID = models.AutoField(primary_key=True)
    creator = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
    appname = models.CharField(max_length=128)
    body = models.TextField(max_length=512)
    downloads = models.IntegerField(default=0)
    createdAt = models.DateTimeField(default=timezone.now)
    lastMod = models.DateField(auto_now=True)
    website = models.URLField(max_length=512, blank=True, null=True)
    contectEmail = models.EmailField(max_length=70)
    sourcefiles = models.FileField(upload_to=user_directory_path, blank=True)
    smallPic = models.ImageField(upload_to=user_directory_path, blank=True)
    bigimg = models.ImageField(upload_to=user_directory_path, blank=True)
    linkImg = models.URLField(max_length=512, blank=True, null=True)
    typOfAccount = models.CharField(
        max_length=4,
        choices=TypeOfUserAccount,
        default='All',
    )
    Fakultaet = models.CharField(
        max_length=4,
        choices=FK,
        default='FK00',
    )
    objects = models.Manager()

    def __str__(self):
      return "APP-Name: " + str(self.appname) + " APP-ID: " + str(self.appID) + " APP-Creator: " + str(self.creator)


'''
Model for the Comments of a APP
'''
class appKomments(models.Model):
    creator = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
    post = models.ForeignKey(APP, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    kommentar = models.CharField(max_length=1024)
    objects = models.Manager()
    createdAt = models.DateTimeField(default=timezone.now)
    lastMod = models.DateField(auto_now=True)

    def __str__(self):
      return "Comment-Title:" + str(self.title) + " Comment-Creator:" + str(self.creator)

'''
UNUSED Methods
class imagesForApp(models.Model):
     img = models.ImageField(upload_to=user_directory_path)
     name = models.TextField()


def get_default_data():
    return { 'null':'null' }
'''