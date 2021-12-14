from django.db import models
from datetime import datetime


# Create your models here.

class Participant(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    favorite_book = models.CharField(max_length=255)
    dunno = models.CharField(max_length=255)


class FormModel(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'form_model: {self.name}'


class FormField(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    form = models.ForeignKey(FormModel, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'Field: {self.name}, model: {self.form.name}'


class FormRecord(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)  # need additional import
    # date = models.DateTimeField(auto_now_add=True) # will be always now(), not what i want


class FormData(models.Model):
    # form_id = models.ForeignKey(FormModel, on_delete=models.CASCADE)
    form_id = models.IntegerField()
    # field_id = models.ForeignKey(FormField, on_delete=models.CASCADE)
    field_id = models.IntegerField()
    value = models.CharField(max_length=255)
    # record_id = models.ForeignKey(FormRecord, on_delete=models.CASCADE)
    record_id = models.IntegerField()
