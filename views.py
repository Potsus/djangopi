import logging
import requests

from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView


class root_view(TemplateView):
    template_name = 'index.html'

    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return TemplateResponse(
            request,
            self.template_name,
            context
        )

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return TemplateResponse(
            request,
            self.template_name,
            context
        )   