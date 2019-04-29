from django_tables2 import tables, TemplateColumn
from inschrijven.models import Lid,Inschrijving,Groep,Leiding,InschrijvingLid
from django.contrib.auth.models import User
from django_tables2_column_shifter.tables import ColumnShiftTable


class LedenTable(tables.Table):
    detail = TemplateColumn(template_name='leden/lid_detail_btn.html')

    class Meta:
        model = Lid

class InschrijvingTable(tables.Table):
    edit = TemplateColumn(template_name='inschrijven/inschrijving_edit_btn.html')
    verwijder = TemplateColumn(template_name='inschrijven/inschrijving_delete_btn.html')

    class Meta:
        model = Inschrijving

class GroepenTable(tables.Table):
    edit = TemplateColumn(template_name='groep/groep_edit_btn.html')

    class Meta:
        model = Groep

class LeidingTable(tables.Table):
    verwijder = TemplateColumn(template_name='leiding/leiding_delete_btn.html')

    class Meta:
        model = Leiding

class UserTable(tables.Table):
    verwijder = TemplateColumn(template_name='leiding/user_del_btn.html')

    class Meta:
        model = User

class InschrijvingLidTable(tables.Table):
    class Meta:
        model = InschrijvingLid

