from rest_framework.decorators import action
from rest_framework.response import Response

class MarkIsCheckMixin:
    @action(detail=True, methods=['post'])
    def mark_is_check(self, request, pk=None):
        instance = self.get_object()
        instance.contain = not instance.contain
        instance.save()
        
        status = 'display' if instance.contain else 'undisplay'
        return Response({'status': status})
