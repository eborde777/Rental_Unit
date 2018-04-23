from django.db import models
# from smart_selects.db_fields import ChainedForeignKey
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

from rental_unit.utils import generate_unique_post_id_and_slug 
# Create your models here.

RENTAL_CHOICES = (
    ('Paying Guest', 'Paying Guest'),
    ('Roommate', 'Roommate'),
    ('Condo', 'Condo'),
    ('House', 'House'),
    ('Apartment', 'Apartment')
)

GENDER_CHOICE = (
    ('male', "Male"),('female', "Female"), ('any', 'Any' )
)

LEASE_CHOICE = (
    ("monthly", "Monthly"), ("three months", "Three Months"),
    ("six months", "Six Months"), ("nine months", "Nine Months"),
    ("one year", 'One Year')
)

SMOKING_CHOICE = (
    ("yes", "YES"), ("no", "NO"), ("outside only", "OUTSIDE ONLY")
)

PET_CHOICE = (
    ("yes", "YES"), ("no", "NO")
)

BATH_CHOICE = (
    ("yes", "YES"), ("no", "NO")
)

ACCOMODATE_CHOICE = (
    ("1", "1"), ("2", "2"),
    ("3", "3"), ("4", "4"), ("5", "5"), ("more than 5", "More than 5")
)

class State(models.Model):
    state_abbrv = models.CharField(max_length=3, null=True)
    state = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.state)

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Cities'



class Post(models.Model):
    rental_type  = models.CharField(max_length = 50, blank=True, null=True, choices=RENTAL_CHOICES)
    title = models.CharField(max_length = 500)
    unique_post_id = models.CharField(max_length=10, blank=True, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add = True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)  
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    cities = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    zip_code = models.CharField(max_length=5)
    available_from = models.DateField()
    accomodates = models.CharField(max_length = 10, choices = ACCOMODATE_CHOICE)
    expected_rent = models.DecimalField(decimal_places=2, max_digits=9)
    posted_by = models.CharField(max_length=150)
    attached_bath = models.CharField(max_length=5, choices = BATH_CHOICE)
    preferred_gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    lease_type = models.CharField(max_length=200, choices = LEASE_CHOICE)
    amenities = models.CharField(max_length=500)
    smoke_policy = models.CharField(max_length=100, choices= SMOKING_CHOICE)
    veg_non_veg_preference = models.CharField(max_length=200)
    pet_friendly = models.CharField(max_length=5, choices = PET_CHOICE)
    furnishing_details = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={'slug':self.slug})


# generating unique post Id and unique slug, and setting it to the corresponding fields before saving into database
@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, *args, **kwargs):

    post_id, new_slug = generate_unique_post_id_and_slug(instance)

    if not instance.unique_post_id:
        instance.unique_post_id = post_id

    if not instance.slug:
        instance.slug = new_slug    


# We could have used django-smart-select
 # cities = ChainedForeignKey(
    #     City,
    #     chained_field="new_state",
    #     chained_model_field="state",
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True
    # )




    
    # state = models.CharField(max_length=30, choices=states_choices) #models.ForeignKey(State, on_delete=models.DO_NOTHING)
    # city = models.CharField(max_length=50) #models.ForeignKey(City, on_delete=models.DO_NOTHING)
    # zip_code = models.CharField(max_length=5) #models.ForeignKey(Zipcode, on_delete=models.DO_NOTHING)
    # available_from = models.DateField()
    # accomodates = models.IntegerField()
    # expected_rent = models.DecimalField(default='0.00', decimal_places=2, max_digits=5)
    # posted_by = models.CharField(max_length=150)
    # room_type = models.CharField(max_length=100)
    # attached_bath = models.BooleanField(default=False)
    # preferred_gender = models.CharField(max_length=10)
    # lease_type = models.CharField(max_length=200)
    # amenities = models.CharField(max_length=500)
    # smoke_policy = models.CharField(max_length=100)
    # veg_non_veg_preference = models.CharField(max_length=200)
    # pet_friendly = models.CharField(max_length=100)
    # furnishing_details = models.TextField()

    # def __str__(self):
    #     return self.title

    # def get_absolute_url(self):
    #     return reverse("posts:detail", kwargs={"slug":self.slug})

   


