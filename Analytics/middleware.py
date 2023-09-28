from django.utils.functional import SimpleLazyObject
from django.contrib.auth.MiddleWare import MiddlewareMixin
from django.contrib.auth import get_user, authenticate

class CustomAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_token = request.META.get('HTTP_X_AUTH_TOKEN')
        
        if auth_token:
            user = authenticate(request, auth_token=auth_token)
            
            if user is not None:
                request.user=user
                