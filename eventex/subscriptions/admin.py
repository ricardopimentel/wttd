from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subcribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('created_at',)

    def subcribed_today(self, obj):
        return obj.created_at.date() == now().date()

    subcribed_today.short_description = 'inscrito hoje?'
    subcribed_today.boolean = True

admin.site.register(Subscription, SubscriptionModelAdmin)