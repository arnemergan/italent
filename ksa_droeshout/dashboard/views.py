from django.views import generic


class dashboardView(generic.TemplateView):
    template_name = 'dashboard_index.html'

