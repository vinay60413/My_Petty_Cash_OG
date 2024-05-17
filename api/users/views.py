"""users views
"""
from django.http import HttpResponse
# Create your views here.
def member(requests):
    """_summary_

    Args:
        requests (_type_): _description_
    """
    return HttpResponse("hello")
