from rest_framework.generics import ListAPIView

from .models import User
from .serializers import UserActivitySerializer


class ActivityList(ListAPIView):
    queryset = User.objects.only('user_id', 'time_zone').filter(is_superuser=False).prefetch_related('useractivity_set')
    serializer_class = UserActivitySerializer

