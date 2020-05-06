from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import User
from .serializers import UserActivitySerializer


class ActivityList(ListAPIView):
    queryset = User.objects.only('user_id', 'time_zone').filter(is_superuser=False).prefetch_related('useractivity_set')
    serializer_class = UserActivitySerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        data_to_return = {'ok': True, 'members': response.data}
        if response.status_code != 200:
            data_to_return = {'ok': False, 'result': response.data}
        return Response(data=data_to_return)
