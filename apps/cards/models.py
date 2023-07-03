from django.db import models
from apps.users.models import MyUser
from apps.admin_panel.models import CardCategories


class Cards(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    card_category_id = models.ForeignKey(CardCategories, on_delete=models.CASCADE)
    card_img = models.ImageField(upload_to='card_img/', null=False, blank=False)
    card_title = models.CharField(max_length=255, null=False, blank=False)
    card_description = models.CharField(max_length=255, null=False, blank=False)
    card_about = models.CharField(max_length=5000, null=False, blank=False)
    instagram = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone_number1 = models.IntegerField(null=False, blank=False)
    phone_number2 = models.IntegerField(null=True, blank=True)
    phone_number3 = models.IntegerField(null=True, blank=True)
