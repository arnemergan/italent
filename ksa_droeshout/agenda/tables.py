from django_tables2 import tables, TemplateColumn
from agenda.models import AgendaItem


class AgendaItemTable(tables.Table):
    edit = TemplateColumn(template_name='edit_agenda_item.html')
    verwijder = TemplateColumn(template_name='delete_agenda_item.html')

    class Meta:
        model = AgendaItem