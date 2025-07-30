from django_components import component

@component.register('title')
class Title(component.Component):
    template_name = 'ui/title.html'
    
    # class Media:
    #     css = 'Title/style.css'
    #     js = 'Title/script.js'