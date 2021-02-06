from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    CAT_TYPE = (
        ("U", "Urban"),
        ("R", "Rural")
    )
    name = models.CharField(max_length=1, choices=CAT_TYPE,
                            default="U", blank=False, null=False)

    def __str__(self):
        return self.name


class District(models.Model):
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name="district_state")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="district_category", default = 1)
    name = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name


class Taluka(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="taluka_district")
    name = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name
