from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm , TextInput



class AllUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='groups_related',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions_related',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    username = None

    choix= (
        ('Medecin','Medecin'),
        ('Patient','Patient'),
        ('Interprete','Interprete')
    )
    c= (
        ('M','Masculin'),
        ('F','Feminin')
    )

    #is_verified = models.BooleanField(default=False)
    date_inscription = models.DateTimeField(auto_now=True)
    name = models.CharField("Entrer votre nom", max_length=50)
    firstname = models.CharField("Entrer votre Prénom", max_length=50)
    genre = models.CharField(max_length=50, choices=c, default = 'M')
    langue = models.CharField("langue", max_length=50)
    email = models.EmailField( max_length=254, unique=True)
    status = models.CharField(max_length=50, choices=choix)
    specialite = models.CharField("Entrer votre specialite", max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "AllUser"
        verbose_name_plural = "AllUsers"

    def __str__(self):
        return self.name

class Consultation(models.Model):
    date = models.DateTimeField("Date de la consultation")
    medecin = models.CharField(max_length=50)
    patient = models.CharField(max_length=50)
    interprete = models.CharField(max_length=50)
    tokken = models.CharField( max_length=50)

    class Meta:
        verbose_name = "Consultation"
        verbose_name_plural = "Consultations"

    def __str__(self):
        return self.name


class Horaire(models.Model):
    choix= (
        ('Lundi','Lundi'),
        ('Mardi','Mardi'),
        ('Mercredi','Mercredi'),
        ('Jeudi','Jeudi'),
        ('Vendredi','Vendredi'),
        ('Samedi','Samedi'),
        ('Dimanche','Dimanche'),
    )
    jours = models.CharField('choisiser votre jour', max_length=50, choices=choix, default='Lundi')
    temp = models.TimeField()
    user = models.ForeignKey(AllUser, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Horaire")
        verbose_name_plural = ("Horaires")

    def __str__(self):
        return self.jours


class Notification(models.Model):
    date = models.DateTimeField( auto_now_add=True)
    user = models.ForeignKey(AllUser, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name = ("Notification")
        verbose_name_plural = ("Notifications")

    def __str__(self):
        return self.user