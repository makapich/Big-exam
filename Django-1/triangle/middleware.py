from django.shortcuts import reverse

from .models import Logs


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not self._is_admin_request(request):
            log = Logs(path=request.path, method=request.method)
            log.get_data = request.GET.dict()
            log.post_data = request.POST.dict()
            log.save()

        response = self.get_response(request)

        return response

    @staticmethod
    def _is_admin_request(request):
        admin_url_prefix = reverse('admin:index').rstrip('/')
        return request.path.startswith(admin_url_prefix)
