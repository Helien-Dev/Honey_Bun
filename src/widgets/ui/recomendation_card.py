from django_components import component
from django.db.models import Q
from catalog.models import Product 

@component.register("recommendation_card")
class RecommendationCard(component.Component):
    template_name = "ui/recommendation_card.html"

    def get_context_data(self, product=None, exclude_id=None, limit=3, category=None, **kwargs):
        """
        Args:
            product: Producto actual (opcional)
            exclude_id: ID del producto a excluir
            limit: Número de productos a mostrar
            category: Filtrar por categoría (si tienes ese campo)
        """

        # Base queryset
        recommendations = Product.objects.all()

        # Excluir producto actual si se proporciona
        if exclude_id:
            recommendations = recommendations.exclude(id=exclude_id)
        elif product and hasattr(product, 'id'):
            recommendations = recommendations.exclude(id=product.id)

        # Filtrar por categoría si se especifica
        if category:
            recommendations = recommendations.filter(category=category)

        # Obtener productos aleatorios
        recommendations = recommendations.order_by("?")[:limit]

        context = {
            "recommendations": recommendations,
            "current_product": product,
            "limit": limit
        }

        return context

    # class Media:
    #     css = {
    #         'all': ('components/recommendation_card/style.css',)
    #     }
    #     js = ('components/recommendation_card/script.js',)
