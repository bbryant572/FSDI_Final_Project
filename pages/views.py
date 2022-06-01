from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home_firstpage.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class MainPageView(TemplateView):
    template_name = "home_loggedin.html"
