from rest_framework import permissions
from .models import Review


class IsReviewOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.review_owner == request.user


class IsUniqueReviewOwner(permissions.BasePermission):
    message = 'You have already submitted a review for this user.'

    def has_permission(self, request, view):
        user = request.user
        review_owner_id = request.data.get('review_owner')
        if user and review_owner_id:
            existing_reviews = Review.objects.filter(user=user, review_owner_id=review_owner_id)
            return not existing_reviews.exists()
        return True
