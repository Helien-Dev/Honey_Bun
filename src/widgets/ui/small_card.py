from django_components import component
from catalog.models import Product

@component.register("small_card")
class SmallCard(component.Component):
    template_name = "ui/small_card.html"
    
    def get_context_data(self, model_instance):
        # Obtener productos en oferta con descuento >= 10%
        model_instance = Product.objects.filter(
            on_offer=True,  # Que esté marcado como en oferta
            offer__gte=10   # Con descuento >= 10%
        )[:2]
        
        context = {"model_data": model_instance}
        return context