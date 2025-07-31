from django_components import component
from django.db.models import Q
from catalog.models import Product 

@component.register("recommendation_card")
class RecommendationCard(component.Component):
    template_name = "ui/recommendation_card.html"

    def get_context_data(self, model_instance):

        model_instance = Product.objects.all().order_by("?")[:3]

        context = {"model_data": model_instance}

        return context


    # class Media:
    #     css = {
    #         'all': ('components/recommendation_card/style.css',)
    #     }
    #     js = ('components/recommendation_card/script.js',)
