from django.contrib import admin
from .models import AppTextos, AppServicos

# Mostra como será descrito os textos do site.
class AppTextosAdmin(admin.ModelAdmin):
    list_display = ('titulo','pagina')
    list_filter = ("pagina",)
    search_fields = ['titulo']
class AppServicosAdmin(admin.ModelAdmin):
    list_display = ('servico','preco')
    list_filter = ("servico",)
    search_fields = ['servico']

admin.site.register(AppTextos,AppTextosAdmin)
admin.site.register(AppServicos,AppServicosAdmin)


