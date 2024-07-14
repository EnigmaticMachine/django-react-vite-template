from django.http import JsonResponse
from django.utils import timezone
from django.db import connections
from django.db.utils import OperationalError
from .models import ErrorLog
from datetime import timedelta


def error_count(request):
    one_hour_ago = timezone.now() - timedelta(hours=1)
    count = ErrorLog.objects.filter(
        timestamp__gte=one_hour_ago, status_code__gte=400
    ).count()
    return JsonResponse({"error_count": count})


def health_check(request):
    db_conn = connections["default"]
    try:
        db_conn.cursor()
    except OperationalError:
        return JsonResponse({"status": "unhealthy"}, status=500)
    return JsonResponse({"status": "healthy"})
