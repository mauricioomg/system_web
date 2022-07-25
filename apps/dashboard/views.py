from django.views import generic


""" HOME """
class IndexView(generic.TemplateView):
    template_name = 'home/index.html'
""" END_HOME """