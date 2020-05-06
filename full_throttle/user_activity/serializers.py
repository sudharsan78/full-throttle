from rest_framework import serializers
from .models import User, UserActivity


class ActivitySerializer(serializers.ModelSerializer):
	start_time = serializers.DateTimeField(format='%b %e %Y  %#I:%M%p')
	end_time = serializers.DateTimeField(format='%b %e %Y  %#I:%M%p')

	class Meta:
		model = UserActivity
		fields = ('start_time', 'end_time')


class UserActivitySerializer(serializers.ModelSerializer):
	id = serializers.CharField(source='user_id')
	real_name = serializers.CharField(source='get_full_name')
	tz = serializers.CharField(source='time_zone')
	activity_periods = ActivitySerializer(source='useractivity_set', read_only=True, many=True)

	class Meta:
		model = User
		fields = ['id', 'real_name', 'tz', 'activity_periods']
