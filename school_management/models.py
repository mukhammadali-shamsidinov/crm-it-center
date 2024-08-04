from django.db import models

# Create your models here.
GENDER = (
    ("MEN","MEN"),
    ("FEMALE","FEMALE")
)
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.CharField(choices=GENDER,blank=True,null=True,max_length=10)
    date_of_bith = models.DateTimeField()
    joining_date = models.DateTimeField()
    phone_number = models.CharField(max_length=11)
    adress = models.TextField()


    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    pass


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Section(models.Model):
    OPTION=(
        ('A','A'),
        ('B', 'B'),
        ('C', 'C'),
    )

    section = models.CharField(max_length=10)

    def __str__(self):
        return self.select

class Academics(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    assign_date = models.DateTimeField()
    submission_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    document = models.FileField()

    def __str__(self):
        return self.title

class HomeWork(Academics):
    send_student = models.BooleanField(default=True)
    send_parent = models.BooleanField(default=False)

    def __str__(self):
        return self.send_parent

EVENT_TITLE = (
    ('Dasturlashga ilk qadam','Dasturlashga ilk qadam'),
    ('Dasturlashni o"rganishdagi xatolar','Dasturlashni o"rganishdagi xatolar')
)
STATUS = (
    ('Approved','Approved'),
    ('Unapproved', 'Unapproved'),
)
class Events(models.Model):

    title = models.CharField(choices=EVENT_TITLE,max_length=150)
    description = models.TextField()
    file = models.FileField()
    status = models.CharField(choices=STATUS,max_length=150)

    def __str__(self):
        return self.title



class Notice(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    select = models.ForeignKey(Section,on_delete=models.CASCADE)
    url = models.URLField()
    file = models.FileField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices=STATUS,max_length=150)

    def __str__(self):
        return self.title





class Settings(models.Model):
    theme_color = models.CharField(max_length=150)
    notification = models.BooleanField(default=False)
    email = models.BooleanField(default=False)

    def __str__(self):
        return self.theme_color










