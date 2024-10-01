from datetime import datetime, timedelta
from django.utils import timezone

from .models import Report, Subject

class Query:
    def get_mytimezone_date(self, original_datetime=None):
        tz = timezone.get_current_timezone()
        if original_datetime:
            #new_datetime = datetime.strptime(original_datetime, '%Y-%m-%d')
            #timezone_datetime = timezone.make_aware(new_datetime, tz)
            timezone_datetime = timezone.make_aware(original_datetime, tz, True)
        else:
            new_datetime = datetime.now()
            timezone_datetime = timezone.make_aware(new_datetime, tz)
        return timezone_datetime

    def __init__(self, start_date=None, end_date=None, d=7):
        if end_date:
            self.end_date = self.get_mytimezone_date(end_date).date()
        else:
            self.end_date = self.get_mytimezone_date()

        if start_date:
            self.start_date = self.get_mytimezone_date(start_date).date()
        else:
            self.start_date = self.end_date - timedelta(days=d)

    def get_report(self, d):
        query = Report.objects.filter(
            create_time__gte=self.start_date,
            create_time__lte=self.end_date
        )
        return query
    
    def get_subject(self, col):
        query = Subject.objects.filter(
            subject_name__in = col
        )
        return query
