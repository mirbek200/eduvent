from django.db import models


class CardCategories(models.Model):
    category_avatar = models.ImageField(upload_to='category_icons/', null=False, blank=False)
    category_name = models.CharField(max_length=255, null=True, blank=True)


class Subcategories(models.Model):
    main_category_id = models.ForeignKey(CardCategories, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=255, null=True, blank=True)
