from import_export import resources
from .models import Lid

class LidResource(resources.ModelResource):
    class Meta:
        model = Lid