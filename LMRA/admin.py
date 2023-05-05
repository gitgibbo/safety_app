from django.contrib import admin

# Register your models here.

from .models import LMRA, Hazard
#admin.site.register(LMRA)
admin.site.register(Hazard)

class HazardInline(admin.StackedInline):
    model = Hazard

@admin.register(LMRA)
class LMRAAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'owner',)
    list_display = ('location', 'owner', 'date_added')
    inlines = [HazardInline]

    """ class Media:
        css = {'all': ('admin/css/widgets.css',)}
        js = ('admin/js/core.js', 'admin/js/RelatedObjectLookup.js', 'admin/js/vendor/jquery/jquery.js', 'admin/js/jquery.init.js')
 """