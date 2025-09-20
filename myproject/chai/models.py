from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# চা ভ্যারাইটি মডেল
class Chaivarieties(models.Model):
    CHAI_TYPE_CHOICE = [
        ('MZ', 'Masala'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chas/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default=' ')

    def __str__(self):
        return self.name

# চা রিভিউ মডেল
class ChaiReview(models.Model):
    chai = models.ForeignKey(Chaivarieties, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'

# স্টোর মডেল (ManyToMany)
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(Chaivarieties, related_name='stores')

    def __str__(self):
        return self.name

# সার্টিফিকেট মডেল (OneToOne)
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(Chaivarieties, on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Certificate for {self.chai.name}'







    

