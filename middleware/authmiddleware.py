from typing import Any
from django.contrib.auth import authenticate


class AnanlyticsAuthenticationMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request) -> Any:
        user = authenticate(request)
        
        if user is not  None:
            request.user = user
        
        response = self.get_response(request)
        
        return response