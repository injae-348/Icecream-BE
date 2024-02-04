from rest_framework import status
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


    def create_with_bank_account(self, request, *args, **kwargs):
        bankAccountId = request.data.get('bankAccountId')

        if not bankAccountId:
            return Response({'error':'bankAccountId is required'},status=status.HTTP_400_BAD_REQUEST)

        instance_data = request.data.copy()
        instance_data['bankAccountId'] = bankAccountId
        serializer = self.get_serializer(data=instance_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)    