from django_components import Component, register

@register("linkedin_icon")
class LinkedinIcon(Component):
    template_name = "components/icons/linkedin_icon.html"
