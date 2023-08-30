"""
This module holds views for root route.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    """
    Return a message when user lands on the root URL.
    :returns: object with key "message"
    :rtype: Response
    """
    return Response({
        "message": "Welcome to my drf API!"
    })
