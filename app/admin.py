from django.contrib import admin
from .models import AppTextos

# Mostra como será descrito os textos do site.
class AppTextosAdmin(admin.ModelAdmin):
    list_display = ('titulo','pagina')
    list_filter = ("pagina",)
    search_fields = ['titulo']

admin.site.register(AppTextos,AppTextosAdmin)


