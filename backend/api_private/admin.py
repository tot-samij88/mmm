import imp
from django.contrib import admin
from .models import PlanInvestment


class PlanInvestmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'profit',
        'min_deposite',
        'max_deposite',
    )
    # search_fields = ('id_request', 'date_create',
    #                  'pair_full', 'address', 'email')
    list_display_links = (
        'id',
        'name',
    )

admin.site.register(PlanInvestment, PlanInvestmentAdmin)
# admin.site.register(StageStatus, StageStatusAdmin)
