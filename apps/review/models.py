from django.db import models
from apps.users.models import MyUser


class Review(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    review_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='review_owner')

