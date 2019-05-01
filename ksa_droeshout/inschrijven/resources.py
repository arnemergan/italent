from import_export import resources
from .models import Lid,InschrijvingLid

class LidResource(resources.ModelResource):
    class Meta:
        model = Lid

# class InschrijvingLidResource(resources.ModelResource):
#     class Meta:
#         model = InschrijvingLid