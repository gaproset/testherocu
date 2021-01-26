from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_to(instance, filename):
    return 'logos/{filename}'.format(filename=filename)

class partnersType(models.Model):

    typename = models.CharField(max_length=120, default="επάγγελμα" ,unique=True)
    # experts = models.ManyToManyField(partners)
    #  last_name = models.CharField(max_length=120, default="Επίθετο")
    #  email = models.EmailField()
    #  partnertype = models.ForeignKey(PartnersType, to_field="name", on_delete=models.SET_NULL, null = True)

    # afm = models.CharField(max_length=12)
    # link = models.CharField(max_length=12)

    # cost = models.DecimalField(default = 0, max_digits=10, decimal_places=2)
    # details = models.CharField(max_length=1200)

    class Meta: 
        app_label = 'ekdilwsi'
        db_table = '_partnersType'
    def _str_(self):
        return self.typename

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 



class partners(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)

    # first_name = models.CharField(max_length=120, default="όνομα")
    # last_name = models.CharField(max_length=120, default="Επίθετο")
    # email = models.EmailField()

    fblink = models.URLField(max_length=120, null = True)
    description = models.CharField(max_length=1200, null = True)

    ptype = models.ForeignKey(partnersType, to_field="typename", on_delete=models.SET_NULL, null = True)

    afm = models.CharField(max_length=12)
    worklink = models.URLField(max_length=120)

    address = models.URLField(max_length=120, default="-")

    cost = models.DecimalField(default = 0, max_digits=10, decimal_places=2)
    details = models.CharField(max_length=1200)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            partners.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.partners.save()

    class Meta: 
        app_label = 'ekdilwsi'
        db_table = '_partners'
    def _str_(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 




# Create your models here.
class Ekdilwsi(models.Model):    
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    info = models.TextField(default = "-")
    place = models.CharField(max_length=200, null=True)
    happeningdate = models.DateTimeField(default=now, blank=True)

    organizer = models.ForeignKey(User, related_name='organizer',  to_field="username", on_delete=models.SET_NULL, null=True)
    partners = models.ManyToManyField(partners, related_name='partners')
    sponsors = models.ManyToManyField(User, related_name='sponsors')

    onetime = models.BooleanField(default=False)
    isfree = models.BooleanField(default=False)
    cost = models.DecimalField(default = 0, max_digits=5, decimal_places=2)

    # duration = models.DurationField(default=int(timedelta(minutes=20).total_seconds()))

    venueneeded = models.BooleanField(default=False)
    costvenue = models.DecimalField(default = 0, max_digits=10, decimal_places=2)

    cateringneeded = models.BooleanField(default=False)
    costperperson = models.DecimalField(default = 0, max_digits=10, decimal_places=2)

    

    # cateringneeded =  isfree = models.BooleanField(default=False)
    # costcaterin = models.DecimalField(default = 0, max_digits=5, decimal_places=2)


    

    class Meta: 
        app_label = 'ekdilwsi'
        db_table = '_ekdilwsi'
    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)   






class Invite(models.Model):

    ekdilwsiinvited = models.ForeignKey(Ekdilwsi, to_field="name",  on_delete=models.SET_NULL, null=True)
    fromUser = models.ForeignKey(User, related_name='fromUser',  to_field="username", on_delete=models.SET_NULL, null=True)
    toUser = models.ForeignKey(User, related_name='toUser',  to_field="username", on_delete=models.SET_NULL, null=True)
    isopened = models.BooleanField(default=False)
    sentdate = models.DateField(default="1991-01-01", blank=True) 
    isAccepted = models.BooleanField(default=False)
    isRejected = models.BooleanField(default=False)
    isDeciding = models.BooleanField(default=False)
    info = models.TextField(default = "-")

    class Meta: 
        app_label = 'ekdilwsi'
        db_table = '_invite'
    def _str_(self):
        return self.ekdilwsiinvited

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 


class library(models.Model):
    name = models.CharField(max_length=120, default="όνομα", unique=True)
    location = models.CharField(max_length=120)
    class Meta: 
        app_label = 'ekdilwsi'
        db_table = '_library'
    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 


class attendancelogger(models.Model):

    first_name = models.CharField(max_length=120, default="όνομα")
    last_name = models.CharField(max_length=120, default="Επίθετο")
    email = models.EmailField()
    credentials = models.CharField(max_length=120, unique=True)
    libraryvisited = models.ForeignKey(library, to_field="name", on_delete=models.SET_NULL, null=True)
    section = models.CharField(max_length=120)
    reason = models.CharField(max_length=120)
    timelogged = models.DateTimeField(default=now, blank=True)

    class Meta: 
        app_label = 'ekdilwsi'
        db_table = '_attendace'
    def _str_(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 










# class ProjectFolder(models.Model):
#     fname = models.CharField(max_length=120, unique=True, default="ΤίτλοςΈργου")
#     project_title = models.CharField(max_length=120)
#     description = models.TextField()

#     completedPF = models.BooleanField(default=False)
#     userId = models.ForeignKey(User, related_name='userId', to_field="username", on_delete=models.SET_NULL, null=True)
#     contractor = models.ForeignKey(User, related_name='contractor',  to_field="username", on_delete=models.SET_NULL, null=True)
#     otherviewers = models.ManyToManyField(User)

#     docsallcounter = models.IntegerField(default=0)  
#     docscompletedcounter = models.IntegerField(default=0)
#     docseditingcounter = models.IntegerField(default=0)
#     projectfoldertype = models.ForeignKey(FolderType, to_field="pfname",  on_delete=models.SET_NULL, null=True)
#     projectdutedate = models.DateField(default="1991-01-01", blank=True) 

#     class Meta: 

#         app_label = 'pwm'
#         db_table = 'pwm_project_folder'
#     def _str_(self):
#         return self.name
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)    

# class Document(models.Model):    
#     docname = models.CharField(max_length=200)
#     docdescription = models.TextField()
#     completed = models.BooleanField(default=False)  
#     editing = models.BooleanField(default=False)
#     unopened = models.BooleanField(default=False)
#     isOriginal = models.BooleanField(default=False)
#     folderId = models.ForeignKey(ProjectFolder, to_field="fname", on_delete=models.SET_NULL, null = True)
#     userId = models.ForeignKey(User, to_field="username",  on_delete=models.SET_NULL, null=True)
#     # fieldsId = models.ManyToManyField(Field)
#     # documentfile = models.FileField(upload_to='uploads/', null = True)
#     fieldsallcounter = models.IntegerField(default=0)  
#     fieldscompletedcounter = models.IntegerField(default=0)
#     docpathstring = models.CharField(max_length=200, default="-")
#     aa =  models.IntegerField(default=0)
#     isMain = models.BooleanField(default=False)
#     docContent = models.TextField(default = "-")
#     main_category = models.IntegerField(default=0)
#     secondary_category = models.IntegerField(default=0)
#     contactorCanView = models.BooleanField(default=False)
#     othersCanView = models.BooleanField(default=False)
#     documentduedate = models.DateField(default="1991-01-01", blank=True) 

    
#     class Meta: 
#         app_label = 'pwm'
#         db_table = 'pwm_document'
#     def _str_(self):
#         return self.docname

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)    
    
# class Field(models.Model):

#     inputtypechoices = [("number", "number"), ("text", "text"), ("email","email"), ("date", "date")]

#     name = models.CharField(max_length =120, unique = True, null = True)
#     fieldType =  models.CharField(max_length=10, choices=inputtypechoices)
#     counter = models.IntegerField(default=0)
#     placeholder = models.TextField()
#     isDefined = models.BooleanField(default=False)
#     isBasic = models.BooleanField(default=False)
#     isGeneral = models.BooleanField(default=False)
#     isTemplate = models.BooleanField(default=True)
#     value = models.TextField(default = '', null = True)
#     folderId = models.ForeignKey(ProjectFolder, to_field="fname", on_delete=models.SET_NULL, null = True)
#     userId = models.ForeignKey(User, to_field="username", on_delete=models.SET_NULL, null = True)
#     docId = models.ManyToManyField(Document)

    
    
#     class Meta: 
#         app_label = 'pwm'
#         db_table = 'pwm_field'

#     def _str_(self):
#         return self.name
        
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)



# class Institute(models.Model):
#     institutename = models.CharField(max_length =120, unique=True, default="όνομα")
#     description = models.TextField()
#     adminInst = models.ForeignKey(User, to_field="username", related_name='adminInst', on_delete=models.SET_NULL, null=True)
#     userId = models.ManyToManyField(User)
#     folderId = models.ManyToManyField(ProjectFolder)
#     docId = models.ManyToManyField(Document)
#     fieldsId = models.ManyToManyField(Field)
    

    

#     class Meta: 
#         app_label = 'pwm'
#         db_table = 'pwm_institute'

#     def _str_(self):
#         return self.name

class Logo( models.Model):
    logo = models.ImageField( upload_to = upload_to, default = "/icon.png")
    institutename = models.ForeignKey(User, to_field="username", on_delete=models.SET_NULL, null=True)

    class Meta: 
        app_label = 'ekdilwsi'
        db_table = '_logo'


