from django_tables2 import tables, TemplateColumn
from inschrijven.models import Lid


class LedenTable(tables.Table):
    detail = TemplateColumn(template_name='leden/lid_detail_btn.html')

    class Meta:
        model = Lid