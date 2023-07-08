from rest_framework import permissions

from apps.review.models import Review


class CanLeaveReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            user_id = request.user.id
            recipient_id = request.data.get('review_owner')
            if recipient_id and Review.objects.filter(user_id=user_id, review_owner_id=recipient_id).exists():
                return False
        return True