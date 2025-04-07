from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
import logging

class RestrictAccessMiddleware(MiddlewareMixin):
    ALLOWED_IPS = ['192.168.1.1', '203.0.113.5']  # Add allowed IPs here
    logger = logging.getLogger(__name__)


    def process_request(self, request):

        
        return JsonResponse({'error': 'NotFound'}, status=404)

