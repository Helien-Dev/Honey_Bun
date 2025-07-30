from django_components import component

@component.register("recomendation_card")
class RecomendationCard(component.Component):
    template_name = "ui/recomendation_card.html"

    # def get_context_data(self, model_instance):

    #     model_instance = Product.objects.all().order_by("?")[:3]

    #     context = {"model_data": model_instance}

    #     return context

    # class Media:
    #     css = "Recomendation_Card/style.css"
    #     js = "Recomendation_Card/script.js"

