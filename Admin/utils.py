from django.utils import timezone
from Admin.models import *

def notification():
    current_time = timezone.now().day
    alert_time = timezone.now().minute

    recent_activity = Activity.objects.filter(time_stamp__day = current_time).order_by('-time_stamp')[:5]
    alert_activity = Activity.objects.filter(time_stamp__minute = alert_time).order_by('-time_stamp')[:1]

    return {'recent_activity': recent_activity, 'alert_activity': alert_activity}