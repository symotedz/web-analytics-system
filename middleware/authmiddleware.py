from typing import Any
from django.contrib.auth import authenticate


class AnanlyticsAuthenticationMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request) -> Any:
        response = self.get_response(request)
        
        return response