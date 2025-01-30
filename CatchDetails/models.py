from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subspecies(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    subspecies_name=models.CharField(max_length=255)

    def __str__(self):
        return self.subspecies_name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=255)
    tackle = models.CharField(max_length=255)
    licensenumber = models.IntegerField()


# SPECIES = [
#     (1, 'Trout'),
#     (2, 'Salmon'),
#     (3, 'Eel'),
#     (4, 'Other'),
#     (5, 'Unknown'),
# ]

TAKEN = [
    (1, 'Taken'),
    (2, 'Released'),
    (3, 'Not Given'),
]

TAG_STATUS = [
    (1, 'Tagged'),
    (2, 'Untagged'),
    (3, 'Newly Tagged Today'),
    (4, 'Not Given'),
]

class Catch(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, name="species")
    subspecies = models.ForeignKey(Subspecies, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images')
    length = models.IntegerField(null=True, blank=True)
    length_guessed = models.BooleanField(default=True)
    weight = models.IntegerField(null=True, blank=True)
    weight_guessed = models.BooleanField(default=True)
    date = models.DateField(null=True, blank=True)
    river = models.CharField(max_length=255, null=True, blank=True)
    tag_status = models.IntegerField(choices=TAG_STATUS, default=4)
    taken_or_released_status = models.IntegerField(choices=TAKEN, default=3)

    # def __str__(self):
    #     return self.species