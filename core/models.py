from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class MO(models.Model):
    area = models.TextField (verbose_name="Округ")
    region = models.CharField (max_length=200, verbose_name="Субъект РФ")
    mo2 = models.CharField (max_length=200, verbose_name="Муниципальное образование")
    # population = models.PositiveIntegerField (blank=True,verbose_name="Население", help_text="Численность населения")
    href = models.URLField(blank=True, null=True, max_length=200)
    path_class = models.CharField (blank=True, null=True, max_length=200, verbose_name="Техническое поле")
    path_d = models.TextField (blank=True, null=True, verbose_name="Координаты")
    path_fill = models.CharField (blank=True, null=True, max_length=200, verbose_name="цвет заполнения")
    path_description_data_img = models.ImageField (upload_to="MO/", blank=True, null=True, verbose_name="Изображение МО")
    path_description_data = models.TextField (blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return f" {self.mo2}"
    
    class Meta:
        verbose_name = "Муниципальное образование"
        verbose_name_plural = "Муниципальные образования"
    
class Service(models.Model):
    name = models.CharField (max_length=200, verbose_name="Название")
    description = models.TextField (blank=True, verbose_name="Описание")
    image = models.ImageField (upload_to="services/", blank=True, verbose_name="Изображение")

    def __str__(self):
        return f" {self.name}"
    
    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Список сервисов"
        ordering = ['description']
    
class Review(models.Model):
    
    TERRIBLE = 1  
    BAD = 2 
    NORMAL = 3 
    GOOD = 4 
    FINE = 5 

    RATING_CHOICES = [
        (TERRIBLE, "Ужасно"),
        (BAD, "Плохо"),
        (NORMAL, "Нормально"),
        (GOOD, "Хорошо"),
        (FINE, "Отлично"),
    ]

    AI_CHOICES = [
    ("ai_checked_true", "Проверено ИИ"),
    ("ai_cancelled", "Отменено ИИ"),
    ("ai_checked_in_progress", "В процессе проверки"),
    ("ai_checked_false", "Не проверено"),
    ]
    
    
    MO = models.ForeignKey ('MO', related_name="mo_name", on_delete=models.SET_NULL,null=True, blank=True, verbose_name="МО")
    service = models.ForeignKey ("Service", related_name="service", on_delete=models.SET_NULL,null=True, blank=True, verbose_name="вид сервиса")
    text = models.TextField (verbose_name="Текст обращения")  
    created = models.DateTimeField (blank=True, null=True, auto_now_add=True, verbose_name="Дата создания")
    rating = models.PositiveSmallIntegerField (blank=True, null=True,choices=RATING_CHOICES, verbose_name="Оценка") 
    is_published = models.BooleanField (blank=True, null=True,default=True, verbose_name="Опубликован")
    ai_checked_status = models.CharField(blank=True, null=True,max_length=30, choices=AI_CHOICES, default="ai_checked_false", verbose_name="Статус ИИ",)
    author = models.CharField (verbose_name="автор сообщения")

    def __str__(self):
        return f"{self.MO}, {self.service},  {self.text}, {self.created}, {self.rating} "

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Список обращений"
        
class Statistics(models.Model):
    period = models.DateTimeField(auto_now_add=True, verbose_name="Отчетный период")
    area = models.TextField (verbose_name="Округ") 
    region= models.ForeignKey ("MO", related_name="region_subject", on_delete=models.SET_NULL,null=True, blank=True, verbose_name="Субъект РФ")
    MO2	= models.TextField (verbose_name="Муниципальное образование второго уровня")
    MO1	= models.TextField (verbose_name="Муниципальное образование первого уровня")
    NNP	= models.TextField (verbose_name="Наименование населенного пункта")
    OKTMO = models.TextField (verbose_name="ОКТМО")
    CHN	= models.DecimalField (verbose_name="Население", help_text="Численность населения", max_digits=10, decimal_places=2)
    GO = models.PositiveSmallIntegerField ( verbose_name="Головной офис") 
    FL = models.PositiveSmallIntegerField ( verbose_name="Филиал") 
    VSP	= models.PositiveSmallIntegerField ( verbose_name="Внутренние структурные подразделения (дополнительные офисы)") 
    PPKO = models.PositiveSmallIntegerField ( verbose_name="Мобильный офис") 
    UTO	= models.PositiveSmallIntegerField ( verbose_name="Удаленные точки обслуживания с работником КО, отличные от окон АО «Почта Банк» в отделениях почтовой связи формата «ОПС Б»") 
    OPSB = models.PositiveSmallIntegerField ( verbose_name="Количество ОПС с окнами ОПС Б") 	
    OPSP1 = models.PositiveSmallIntegerField ( verbose_name="Количество ОПС с окнами ОПС П1") 	
    OPSS = models.PositiveSmallIntegerField ( verbose_name="Количество ОПС с окнами ОПС С") 	
    OPSP2 = models.PositiveSmallIntegerField ( verbose_name="Количество ОПС с окнами ОПС П2") 	
    SOPS = models.PositiveSmallIntegerField ( verbose_name="Стационарное отделение организации федеральной почтовой связи ") 	
    POPS = models.PositiveSmallIntegerField ( verbose_name="Передвижное отделение организации федеральной почтовой связи") 	
    MOB	 = models.PositiveSmallIntegerField ( verbose_name="Мобильные менеджеры кредитных организаций")
    BKKO_NViNPiBO = models.PositiveSmallIntegerField ( verbose_name="Банкоматы КО типа БК c одновременным наличием функций НВ, НП и БО ")	
    BKBPA_NViNPiBO = models.PositiveSmallIntegerField ( verbose_name="Банкоматы БПА (субагентов) типа БК c одновременным наличием функций НВ, НП и БО ")	
    BKKO_NViBO_NP = models.PositiveSmallIntegerField ( verbose_name="Банкоматы КО типа БК с функциями НВ и БО, но без функции НП")	
    BKKO_NViNP_BO = models.PositiveSmallIntegerField ( verbose_name="Банкоматы КО типа БК с функциями НВ и НП, но без функции БО")	
    BKBPA_NViBO_NP = models.PositiveSmallIntegerField ( verbose_name="Банкоматы БПА типа БК с функциями НВ и БО, но без функции НП")	
    BKBPA_NViNP_BO = models.PositiveSmallIntegerField ( verbose_name="Банкоматы БПА типа БК с функциями НВ и НП, но без функции БО")	
    BKKO_NV = models.PositiveSmallIntegerField ( verbose_name="Банкоматы КО типа БК с функцией НВ, при этом функции НП и БО отсутствуют")	
    BKBPA_NV = models.PositiveSmallIntegerField ( verbose_name="Банкоматы БПА (субагентов) типа БК с функцией НВ, при этом функции НП и БО отсутствуют")	
    BKKO = models.PositiveSmallIntegerField ( verbose_name="Банкоматы КО типа БК без функции НВ, но с функцией НП и с функцией БО")	
    BKBPA = models.PositiveSmallIntegerField ( verbose_name="Банкоматы БПА (субагентов) типа БК без функции НВ, но с функцией НП и с функцией БО")	
    BKKO_1 = models.PositiveSmallIntegerField ( verbose_name="Банкоматы КО типа БК без функции НВ и без функции НП, но с функцией БО (платежные терминалы)")	
    BKBPA_1 = models.PositiveSmallIntegerField ( verbose_name="Банкоматы БПА (субагентов) типа БК без функции НВ и без функции НП, но с функцией БО (платежные терминалы)")	
    BPKO = models.PositiveSmallIntegerField ( verbose_name="Банкоматы КО типа БП и иные банкоматы БК без НВ и БО, при этом устройства только с НЮ не учитываются")	
    BPBPA = models.PositiveSmallIntegerField ( verbose_name="Банкоматы БПА (субагентов) типа БП и иные банкоматы БК без НВ и БО, при этом устройства только с НЮ не учитываются")	
    T_BOiNViNP = models.PositiveSmallIntegerField ( verbose_name="Терминалы КО с одновременным наличием функций БО, НВ и НП")		
    T_NV = models.PositiveSmallIntegerField ( verbose_name="Терминалы КО не менее 2х видов операций, при этом есть НВ* (за исключением терминалов КО, указанных в предыдущем столбце)")	
    T_noNV = models.PositiveSmallIntegerField ( verbose_name="Терминалы КО не менее 2х видов операций, при этом нет НВ")	
    T_BO = models.PositiveSmallIntegerField ( verbose_name="Терминалы КО с одной функцией и это не НВ ")	
    MT_BOiNViNP = models.PositiveSmallIntegerField ( verbose_name="МПКТ КО с одновременным наличием функций БО, НВ и НП")	
    MT_NV = models.PositiveSmallIntegerField ( verbose_name="МПКТ КО не менее 2х видов операций, при этом есть НВ* (за исключением терминалов КО, указанных в предыдущем столбце)")	
    MT_noNV = models.PositiveSmallIntegerField ( verbose_name="МПКТ КО не менее 2х видов операций, при этом нет НВ")	
    MT_BO = models.PositiveSmallIntegerField ( verbose_name="МПКТ КО с одной функцией и это не НВ ")	
    KBPA = models.PositiveSmallIntegerField ( verbose_name="Кассы БПА (субагентов), которые не были учтены как терминалы")	
    MFO = models.PositiveSmallIntegerField ( verbose_name="Подразделения микрофинансовых организаций")	
    KPK = models.PositiveSmallIntegerField ( verbose_name="Подразделения кредитных потребительских кооперативов")	
    SKPK = models.PositiveSmallIntegerField ( verbose_name="Подразделения сельскохозяйственных кредитных потребительских кооперативов ")	
    SSD = models.PositiveSmallIntegerField ( verbose_name="Подразделения субъектов страхового дела")	
    I2G = models.PositiveSmallIntegerField ( verbose_name="2G (GSM), 1-да, 0 - нет")	
    I3G = models.PositiveSmallIntegerField ( verbose_name="3G (UMTS), 1-да, 0 - нет")
    I4G = models.PositiveSmallIntegerField ( verbose_name="4G (LTE), 1-да, 0 - нет")
    INTN = models.PositiveSmallIntegerField ( verbose_name="Скорость передачи данных не менее 2048 Кб/с для неподвижных объектов, 1-да, 0 - нет")	
    Time  = models.PositiveSmallIntegerField ( verbose_name="Время, затрачиваемое на поездку общественным или личным транспортом из центра населенного пункта до ближайшего стационарного подразделения кредитной организации без учета затруднений, которые могут возникнуть в пути, мин")
    Time1 = models.PositiveSmallIntegerField ( verbose_name="Время, затрачиваемое на поездку общественным или личным транспортом из центра населенного пункта до ближайшего банкомата с функцией выдачи наличных без учета затруднений, которые могут возникнуть в пути, мин")		
    CHNS = models.PositiveIntegerField (verbose_name="Население субъекта", help_text="Численность населения субъекта")	
    SM = models.PositiveIntegerField (verbose_name="Площадь субъекта", help_text="Площадь субъекта, км2")
    PS = models.PositiveIntegerField (verbose_name="Плотность субъекта (чел/км2)", help_text="Плотность субъекта (чел/км2)")	
    SMRF = models.PositiveIntegerField (verbose_name="Площадь РФ", help_text="Площадь РФ, км2")
    PR = models.PositiveIntegerField (verbose_name="Плотность РФ (чел/км2)")	
    F = models.FloatField(verbose_name="Коэффициент финансовой доступности")	
    TNP	= models.TextField (verbose_name="ОКТМО", help_text="Плотность субъекта (чел/км2)")
    F_NP = models.TextField (verbose_name="F_NP", help_text="Значение F населенного пункта с более высоким коэффициентом F, находящегося не более чем в 2 км от данного, в случае наличия беспрепятственного доступа к нему  пешком в течение не более чем за 20 минут (заполняется для населенных пунктов, в которых F пр < 46%)")	
    F_TD = models.PositiveIntegerField (verbose_name="F_TD", help_text="Наличие в населенном пункте точки доступа к финансовым услугам (компьютер с выходом в интернет), 1- да, 0 - нет (заполняется для населенных пунктов, в которых F пр < 46%); учитывается если F_NP=0  в данном НП или рядом отсутстуют офисы или банкоматы с НВ")

class StatisticsShort(models.Model):
    MO = models.ForeignKey(MO, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Муниципальное образование второго уровня")
    period = models.DateTimeField(auto_now_add=True, verbose_name="Отчетный период")
    MO2	= models.TextField (verbose_name="Муниципальное образование второго уровня")
    MO1	= models.TextField (verbose_name="Муниципальное образование первого уровня")
    F = models.FloatField(verbose_name="Коэффициент финансовой доступности")
    FG = models.FloatField(verbose_name="Коэффициент финансовой грамотности")
    CHN	= models.FloatField (verbose_name="Население", help_text="Численность населения")
    CHN_Sub	= models.FloatField (verbose_name="Население", help_text="Численность населения")
    Pop_Per	= models.FloatField (verbose_name="Население", help_text="Численность населения")
    
    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "отчеты"

    # MO2	= models.TextField (verbose_name="Муниципальное образование второго уровня")

class ReviewAnswer(models.Model):
    Review = models.ForeignKey ('Review', related_name="review_id", on_delete=models.SET_NULL,null=True, blank=True, verbose_name="Идентификатор обращения")
    answer_text = models.TextField (verbose_name="Текст ответа") 
    answer_created = models.DateTimeField (blank=True, null=True, auto_now_add=True, verbose_name="Дата создания") 
    answer_is_published = models.BooleanField (blank=True, null=True,default=True, verbose_name="Опубликован")    
    answer_author = models.CharField (verbose_name="автор ответа")
    
    def __str__(self):
        return f"{self.Review}, {self.answer_text},  {self.answer_created}, {self.answer_author} "

    class Meta:
        verbose_name = "Ответ на обращение"
        verbose_name_plural = "Ответы на обращения"