from django.views import generic
from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar
from calendar import calendar

from .models import AgendaItem

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'agenda_items_list'
    
    def get_queryset(self):
        return AgendaItem.objects.order_by('datumvan')[:6]

class AgendaItemView(generic.DetailView):
    template_name = 'agenda_item.html'
    model = AgendaItem
    
class AgendaView(generic.ListView):
    template_name = 'agenda.html'
    context_object_name = 'agenda_items_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = datetime.today()

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        d = datetime.today()
        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)
        return context

    def prev_month(*d):
        first = d.replace(day=1)
        prev_month = first - timedelta(days=1)
        month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
        return month

    def next_month(*d):
        days_in_month = calendar.monthrange(d.year, d.month)[1]
        last = d.replace(day=days_in_month)
        next_month = last + timedelta(days=1)
        month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
        return month

    def get_date(*req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split('-'))
            return date(year, month, day=1)
        return datetime.today()

    def get_queryset(self):
        return AgendaItem.objects.order_by('datumvan')[:6]

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self,day,events):
        events_per_day = events.filter(datumvan__day=day)
        d = ''
        text = ''
        for event in events_per_day:
            if day != 0:
                text += f'<div class="home-agenda-card card col-lg-12"><div class="card-body">'
                text += f'<h5>{event.titel}</h5>'
                if event.datumvan == event.datumtot:
                  text += f'<h5>{event.datumvan}</h5>'
                else:
                    text += f'<h5>{event.datumvan} - {event.datumtot}</h5>'
                text += f'<form action="/agenda/{event.id}/"> <button class="agenda-item-meer-info">meer info</button></form></div></div>'
        return f"<td><span class='date'>{day}</span><ul> {d} </ul>{text}</td>"

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self,withyear=True):
        events = AgendaItem.objects.filter(datumvan__year=self.year, datumvan__month=self.month)

        cal = f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal