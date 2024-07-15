import logging
from django.conf import settings
from django.http import HttpResponseForbidden
from core.models import ErrorLog

logger = logging.getLogger(__name__)


class LogHttpRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code >= 400:
            # Log to database
            ErrorLog.objects.create(
                method=request.method,
                path=request.path,
                status_code=response.status_code,
            )
            # Also log to the console or file
            logger.info(
                "HTTP Response",
                extra={
                    "method": request.method,
                    "path": request.path,
                    "status_code": response.status_code,
                },
            )
        return response


class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/error-count/":
            token = request.headers.get("Authorization")
            if token != f"Token {settings.GATUS_MONITORING_TOKEN}":
                return HttpResponseForbidden()
        return self.get_response(request)
