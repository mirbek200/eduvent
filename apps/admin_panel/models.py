from django.db import models


class CardCategories(models.Model):
    category_avatar = models.ImageField(upload_to='media/category_icons/', null=False, blank=False)
    category_name = models.CharField(max_length=255, null=True, blank=True)

