from django.db import models

# Create your models here.
class user(models.Model):
        USER_ROLES = [
        ("translator", "Translator"),
        ("client", "Client"),
        ],
        first_name = models.CharField(max_length=255, blank=True)
        last_name = models.CharField(max_length=255, blank=True)
        phone_number = models.IntegerField(max_length=15, blank=True)
        type = models.CharField(max_length=255, choices=USER_ROLES)
        ielts_rank = models.IntegerField(max_length=15, blank=True)
        price = models.CharField(max_length=255, blank=True)
        languages = models.CharField(max_length=255, blank=True)
        template_text = models.CharField(max_length=255, blank=True)
