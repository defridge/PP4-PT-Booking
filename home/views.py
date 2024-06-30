from django.views.generic import TemplateView


class Index(TemplateView):
    """
    View for rendering the home page

    Attributes:
        template_name (str): The template to be used
        for rendering the home page
    """
    template_name = 'home/index.html'
