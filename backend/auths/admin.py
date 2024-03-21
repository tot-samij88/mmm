from django.contrib import admin
from .models import PaymentMethod, TwoFA_keys, ExmoneyUser, UsersLogins, InvitedUsers, ReferralBonuses
from django.contrib.auth.admin import UserAdmin


admin.site.register(TwoFA_keys)
admin.site.register(ExmoneyUser)
admin.site.register(PaymentMethod)
admin.site.register(UsersLogins)
admin.site.register(InvitedUsers)
admin.site.register(ReferralBonuses)
