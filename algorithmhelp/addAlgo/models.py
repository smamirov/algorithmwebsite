from django.db import models

# Create your models here.
class addAlgorithm(models.Model):
    name = models.CharField("Name of Algorithm", max_length=30, blank=False, default=' ')
    timeComplexity = models.CharField("Time Complexity", max_length=30, blank=False, default=' ')
    spaceComplexity = models.CharField("Space Complexity", max_length=30, blank=True)
    description = models.TextField("Description", blank=True)
    applications = models.CharField("Applications", max_length=200, blank=True)
    implementation = models.TextField("Implementation", blank=True)
    output = models.TextField("Output", blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self) 