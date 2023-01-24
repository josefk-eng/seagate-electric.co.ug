from django import template

register = template.Library()


@register.filter
def service_images(images, service):
    filtered = images.filter(service=service)
    return list(filtered)
