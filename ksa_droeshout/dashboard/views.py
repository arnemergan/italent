from django.views import generic


class dashboardView(generic.ListView):
    template_name = 'dashboard_index.html'

    def get_queryset(self):
        return 'tset'
