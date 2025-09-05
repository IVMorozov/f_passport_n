from django.contrib import admin

# Register your models here.
from .models import StatisticsShort, Review, Service, MO, ReviewAnswer

admin.site.register(StatisticsShort)
admin.site.register(MO)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(ReviewAnswer)
