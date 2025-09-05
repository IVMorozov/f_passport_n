from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from .forms import ReviewModelForm, UserRegisterForm, UserLoginForm, ReviewAnswerModelForm
from django.db.models import Avg, Sum, Count
from django.contrib.auth import login, logout as auth_logout, authenticate, get_user_model
import pandas as pd
from django.db.models import F
from .models import MO, StatisticsShort, Review, ReviewAnswer
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views import View

from django.contrib.auth.views import (
    LogoutView,
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


class LandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ФД&ФГ" 
        context["MO"] = MO.objects.all()     
        fd = StatisticsShort.objects.values("MO2").annotate(avg_F=Avg('F')).annotate(avg_FG=Avg('FG')).annotate(avg_CHN=Avg('CHN')).annotate(path_class=F('MO__path_class'))
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
        mo_id = self.kwargs.get('mo_id')  # Извлекаем mo_id из URL
        mo = StatisticsShort.objects.filter(MO=mo_id)  # Получаем все объекты по mo_id
        mo_head = StatisticsShort.objects.values("MO2").annotate(avg_F=Avg('F')).annotate(avg_FG=Avg('FG')).annotate(avg_CHN=Avg('CHN')).filter(MO=mo_id)
        context['mo'] = mo  # Добавляем объект в контекст
        for item in context['mo']:
            item.F = float(item.F.replace(',', '.'))  # Заменяем запятую на точку и преобразуем в число
            item.FG = float(item.FG.replace(',', '.'))
        context['mo_head'] = mo_head
        return context 

class MO_City_View(TemplateView):
    model = StatisticsShort
    template_name = "MO_City.html"
    context_object_name = 'mo'
    pk_url_kwarg = "mo_id"    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mo_id = self.kwargs.get('mo_id')  # Извлекаем mo_id из URL
        mo = StatisticsShort.objects.filter(MO=mo_id).order_by('FG')  # Получаем все объекты по mo_id
        mo_head = StatisticsShort.objects.values("MO2").annotate(avg_F=Avg('F')).annotate(avg_FG=Avg('FG')).annotate(avg_CHN=Avg('CHN')).filter(MO=mo_id)
        context['mo'] = mo  # Добавляем объект в контекст
        for item in context['mo']:
            item.F = float(item.F.replace(',', '.'))  # Заменяем запятую на точку и преобразуем в число
            item.FG = float(item.FG.replace(',', '.'))
        context['mo_head'] = mo_head
        return context 

class RegionReport(TemplateView):
    template_name = "region.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Region" 
        region = StatisticsShort.objects.values("MO2").annotate(avg_F=Avg('F')).annotate(avg_FG=Avg('FG')).annotate(avg_CHN=Avg('CHN')).order_by('-avg_CHN')
        context["region"] = region
        region_head = StatisticsShort.objects.values("MO2").annotate(avg_F=Avg('F')).annotate(avg_FG=Avg('FG')).annotate(avg_CHN=Avg('CHN'))
        region_sum_CHN = sum(item['avg_CHN'] for item in region_head)
        context['region_avg_F'] = sum(item['avg_F'] * item['avg_CHN'] for item in region_head) / (region_sum_CHN)
        context['region_avg_FG'] = sum(item['avg_FG'] * item['avg_CHN'] for item in region_head) / (region_sum_CHN)
        context['region_sum_CHN'] = region_sum_CHN
        context["region_head"] = region_head     
        return context
    
class ReviewView(ListView):
    model = Review
    template_name = "reviews.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Обращения"      
        if self.request.user.is_superuser:
            reviews = Review.objects.all().order_by('-created')            
        else:
            reviews = Review.objects.filter(author=self.request.user.username).order_by('-created')
            
        context["reviews"] = reviews
        review_answers = ReviewAnswer.objects.all().order_by('answer_created')
        context["review_answers"] = review_answers
        


        return context
    
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewModelForm
    template_name = "review_form.html"
    success_url = reverse_lazy("landing")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["title"] = "Оставить обращение"
        context["button_text"] = "Отправить обращение"
        return context    
    
    def form_valid(self, form):
        form.instance.author = self.request.user.username  # Автоматически заполняем поле author
        self.success_url = reverse_lazy('landing')
        messages.success(self.request, "Обращение успешно отправлено")
        return super().form_valid(form)

    
    def form_invalid(self, form):
        # Отправляем сообщение об ошибке
        messages.error(self.request, "Форма заполнена некорректно")
        return super().form_invalid(form)
    
class ReviewAnswerCreateView(CreateView):
    model = ReviewAnswer
    form_class = ReviewAnswerModelForm
    template_name = "answer_form.html"
    success_url = reverse_lazy("reviews")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["title"] = "Оставить обращение"
        context["button_text"] = "Ответить на обращение"
        context["review_id"] = self.kwargs.get('pk')
        return context    
    
    def form_valid(self, form):
        form.instance.answer_author = self.request.user.username  # Автоматически заполняем поле author
        review_id = self.kwargs.get('pk')  # Получите review_id из URL
        form.instance.Review = Review.objects.get(id=review_id)  # Получите экземпляр Review
        self.success_url = reverse_lazy('reviews')
        messages.success(self.request, "Ответ успешно отправлен")
        return super().form_valid(form)

    
    def form_invalid(self, form):
        # Отправляем сообщение об ошибке
        messages.error(self.request, "Форма заполнена некорректно")
        return super().form_invalid(form)
    
class NewLogoutView(LogoutView):    
    template_name = "logout.html"    
    next_page = "logout"

class RegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):
        # Сохраняем пользователя
        user = form.save()
        # Message
        messages.success(
            self.request,
            f"Добро пожаловать, {user.username}! Вы успешно зарегистрировались.",
        )
        # Выполяем авторизацию
        login(self.request, user)
        # Вызываем родительский метод
        return redirect("landing")

    def form_invalid(self, form):
        # Добавляем сообщение об ошибке
        messages.error(self.request, "Пожалуйста, исправьте ошибки в форме.")
        return super().form_invalid(form)

class NewLoginView(LoginView):
    template_name = "login.html"
    authentication_form = UserLoginForm
    redirect_field_name = "landing"
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Вызывается при успешной аутентификации."""
        # Получаем залогиненного пользователя
        user = form.get_user()
        # Добавляем сообщение об успехе
        messages.success(self.request, f"Добро пожаловать, {user.username}!")
        # Вызываем родительский метод, который выполняет вход и редирект
        
        return super().form_valid(form)
        # return login_required(view_func, redirect_field_name="orders_list")(request, *view_args, **view_kwargs)
    

    def form_invalid(self, form):
        """Вызывается, если форма невалидна (ошибка входа)."""
        # Добавляем сообщение об ошибке
        messages.error(self.request, "Неверное имя пользователя или пароль")
        # Вызываем родительский метод, который снова рендерит страницу с формой
        
        return super().form_invalid(form)

class importView(View):
    # def __init__(self, file_path):
    #     self.file_path = file_path
    
    def get(self, request):
        # Логика для обработки GET-запроса
        return render(request, 'import.html')

    def post(self, request):
        # Логика для обработки POST-запроса (например, загрузка файла)
        pass

    def load_data(self):
        try:
            # Чтение данных из Excel
            data = pd.read_excel(self.file_path, skiprows=4)

            # Сохранение данных в базу данных
            for index, row in data.iterrows():
                StatisticsShort.objects.create(
                    field1=row['Column1'],
                    field2=row['Column2'],
                    # Добавьте остальные поля
                )
            return "Данные успешно загружены"
        except Exception as e:
            return f"Ошибка при загрузке данных: {e}"
        

