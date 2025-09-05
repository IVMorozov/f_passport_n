from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Avg
from django.db.models import F
from .models import MO, StatisticsShort
from django.urls import reverse, reverse_lazy

class LandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ФД&ФГ" 
        context["MO"] = MO.objects.all()     
        fd = StatisticsShort.objects.values("MO2").annotate(avg_F=Avg('F')).annotate(avg_FG=Avg('FG')).annotate(avg_Pop_Per=Avg('Pop_Per')).annotate(path_class=F('MO__path_class'))
        context["FD"] = fd
        context["js"] = list(fd)  # Преобразуем QuerySet в список для JSON
        return context

class MO_View(TemplateView):
    template_name = "MO.html"
    model = StatisticsShort
    context_object_name = 'mo'
    pk_url_kwarg = "mo_id"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mo = self.object  # Получаем текущий объект 
        # mo = StatisticsShort.objects.all().filter(MO = 3) 
        context['mo'] = mo  # Получаем все связанные услуги
        # context['order_sum'] = sum(service.price for service in services)        
        return context

class MO_City_View(TemplateView):
    model = MO
    template_name = "MO_City.html"
    context_object_name = 'mo'
    pk_url_kwarg = "mo_id"    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # mo = self.object  # Получаем текущий объект 
        mo = StatisticsShort.objects.all().filter(MO = 9) 
        context['mo'] = mo  # Получаем все связанные услуги
        # context['order_sum'] = sum(service.price for service in services)        
        return context
    