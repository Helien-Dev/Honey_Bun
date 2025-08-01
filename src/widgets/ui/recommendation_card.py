from django_components import component
from django.db.models import Q
from catalog.models import Product
from django.core.paginator import Paginator

@component.register("recommendation_card")
class RecommendationCard(component.Component):
    template_name = "ui/recommendation_card.html"
    
    def get_context_data(self, model_instance=None, page=1, per_page=3):
        # Asegurarse de que page sea un entero
        try:
            page = int(page)
        except (ValueError, TypeError):
            page = 1
            
        # Obtener productos de forma consistente (sin order_by("?") que es random)
        all_products = Product.objects.all().order_by('id')  # Orden consistente
        
        paginator = Paginator(all_products, per_page)
        
        # Usar get_page en lugar de page() para manejar errores automáticamente
        page_obj = paginator.get_page(page)
        
        context = {
            "model_data": page_obj.object_list,
            "page_obj": page_obj,
            "paginator": paginator,
            "current_page": page,
        }
        return context