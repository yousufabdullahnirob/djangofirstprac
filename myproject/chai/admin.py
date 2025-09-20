from django.contrib import admin
from .models import Chaivarieties, ChaiReview, Store, ChaiCertificate


class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2


class ChaivarietiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    inlines = [ChaiReviewInline]
 

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
   

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')


admin.site.register(Chaivarieties, ChaivarietiesAdmin)
admin.site.register(ChaiReview)  
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)


