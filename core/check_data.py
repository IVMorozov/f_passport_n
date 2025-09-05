import os
import django
from django.conf import settings

# Установка настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fd_fg_passport.settings")
django.setup()

from core.models import MO, StatisticsShort

def check_data():
    # Проверка данных в модели MO
    mo_records = MO.objects.all()
    print("Записи из модели MO:")
    for record in mo_records:
        print(record.area, record.region, record.mo2)

    # Проверка данных в модели StatisticsShort
    statistics_short_records = StatisticsShort.objects.all()
    print("Записи из модели StatisticsShort:")
    for record in statistics_short_records:
        print(record.MO2, record.MO1, record.F)

if __name__ == "__main__":
    check_data()
