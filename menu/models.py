from django.contrib import admin
from django.db import models

# Create your models here.
class MenusModel(models.Model):
    title = models.CharField('Menu Name', max_length=50)
    options = models.JSONField('Options')
    """
    Options in DataBase writing in below format:
    {
    "http://site.com/one":   "Option 1",
    "http://site.com/two":   "Option 2",
    "http://site.com/three": "Option 3",
    "http://site.com/four":  ["Option 3", "Suboption 1"],
    "http://site.com/five":  ["Option 3", "Suboption 2"],
    "http://site.com/six":   ["Option 3", "Suboption 3"],
    "http://site.com/seven": ["Option 3", "Suboption 3", "Subsuboption 1"],
    "http://site.com/eight": "Option 4"
    }
    """

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

class MenusAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)