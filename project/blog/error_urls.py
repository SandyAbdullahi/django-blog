from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path
from .views import error404


def response_error_handler(request, exception=None):
    return HttpResponse('Error handler content', status=404)


def permission_denied_view(request):
    raise PermissionDenied


urlpatterns = [
    
    path('*', error404),
]

handler404 = response_error_handler



# ROOT_URLCONF must specify the module that contains handler403 = ...
@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):

    def test_handler_renders_template_response(self):
        response = self.client.get('/403/')
        # Make assertions on the response here. For example:
        self.assertContains(response, 'Error handler content', status_code=403)