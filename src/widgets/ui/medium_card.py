from django_components import component


@component.register("medium_card")
class MediumCard(component.Component):
    template_name = "ui/medium_card.html"

    # def get_context_data(self, model_instance):

    #     model_instance = Product.objects.all().order_by("?")[:3]

    #     context = {"model_data": model_instance}

    #     return context

    # class Media:
    #     css = "Medium_Card/style.css"
    #     js = "Medium_Card/script.js"