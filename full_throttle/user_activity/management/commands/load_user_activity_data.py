import csv
import json
from django.core.management.base import BaseCommand, CommandError
from user_activity.models import User, UserActivity


class Command(BaseCommand):
    help = 'Create user and user activity records from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='input file should be in CSV format')

    def handle(self, *args, **options):
        file_path = options['file_path']

        try:
            csv_file = open(file_path)
        except FileNotFoundError:
            raise CommandError('Could not find file')

        file_data = csv.DictReader(csv_file)
        for data in file_data:
            data = dict(data)
            first_name, last_name = data['user_name'].split()
            user_obj = User.objects.create(username=data['user_name'], first_name=first_name, last_name=last_name,
                                user_id=data['user_id'], time_zone=data['time_zone'])

            activity_data_list = json.loads(data['activity_periods'])
            for activity_data in activity_data_list:
                UserActivity.objects.create(user=user_obj, start_time=activity_data['start_time'],
                                            end_time=activity_data['end_time'])

        csv_file.close()
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
