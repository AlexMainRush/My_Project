from django.contrib import admin
from solo.admin import SingletonModelAdmin
from.models import GlobalSet


@admin.register(GlobalSet)
class GlobalSetAdmin(SingletonModelAdmin):
    pass
