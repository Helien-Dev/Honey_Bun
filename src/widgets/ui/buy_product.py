from django_components import component

@component.register('buy_product')
class BuyProduct(component.Component):
    template_name = 'ui/buy_product.html'