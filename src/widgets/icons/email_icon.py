from django_components import Component, register

@register("email_icon")
class EmailIcon(Component):
    template_name = "components/icons/email_icon.html"
