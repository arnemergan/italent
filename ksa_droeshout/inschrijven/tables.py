from django_tables2 import tables, TemplateColumn
from inschrijven.models import Lid,Inschrijving


class LedenTable(tables.Table):
    detail = TemplateColumn(template_name='leden/lid_detail_btn.html')

    class Meta:
        model = Lid

class InschrijvingTable(tables.Table):
    edit = TemplateColumn(template_name='inschrijven/inschrijving_edit_btn.html')
    verwijder = TemplateColumn(template_name='inschrijven/inschrijving_delete_btn.html')

    class Meta:
        model = Inschrijving
