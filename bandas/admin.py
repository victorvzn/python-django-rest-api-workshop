from django.contrib import admin
from django.utils.html import mark_safe
from .models import Banda, Genero

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
  list_display = ('portada_preview', 'nombre', 'genero',) 
  list_filter = ('genero',)
  search_fields = ('nombre',)
  
  def portada_preview(self, obj):
    if obj.portada:
      return mark_safe(f"<img src='{obj.portada}' width='60' height='60' style='object-fit: cover; border-radius: 4px;'/>")
    return "-"

  portada_preview.short_description = 'Portada'
  portada_preview.admin_order_field = 'portada'