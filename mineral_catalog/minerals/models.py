from django.db import models

# Create your models here.


class Mineral(models.Model):
    """
        Not all entries will have every field as shown in the json file in "mineral_data/mineral.json"
    """
    name = models.CharField(max_length=255, blank=True, default='')
    image_filename = models.CharField(max_length=255, blank=True, default='')
    image_caption = models.TextField(blank=True, default='')
    category = models.CharField(max_length=255, blank=True, default='')
    formula = models.CharField(max_length=255, blank=True, default='')
    strunz_classification = models.CharField(max_length=255, blank=True, default='')
    color = models.CharField(max_length=255, blank=True, default='')
    crystal_system = models.CharField(max_length=255, blank=True, default='')
    unit_cell = models.CharField(max_length=255, blank=True, default='')
    crystal_symmetry = models.CharField(max_length=255, blank=True, default='')
    cleavage = models.CharField(max_length=255, blank=True, default='')
    mohs_scale_hardness = models.CharField(max_length=255, blank=True, default='')
    luster = models.CharField(max_length=255, blank=True, default='')
    streak = models.CharField(max_length=255, blank=True, default='')
    diaphaneity = models.CharField(max_length=255, blank=True, default='')
    optical_properties = models.CharField(max_length=255, blank=True, default='')
    refractive_index = models.CharField(max_length=255, blank=True, default='')
    crystal_habit = models.CharField(max_length=255, blank=True, default='')
    specific_gravity = models.CharField(max_length=255, blank=True, default='')
    group = models.CharField(max_length=255, blank=True, default='')
