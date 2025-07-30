from django_components import component

@component.register('add_to_cart')
class AddToCart(component.Component):
    template_name = 'ui/add_to_cart.html'
