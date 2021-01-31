from django.contrib import admin
from .models import Band, Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'instrument')
    list_filter = ('band',)


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'can_rock')


admin.site.register(Band, BandAdmin)
admin.site.register(Member, MemberAdmin)  # Use the customized options