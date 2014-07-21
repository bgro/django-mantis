from django.conf import settings

def mantis_show_toolbar(request):
    if 'Campaign' in request.path:
        return False
    if request.META.get('REMOTE_ADDR', None) not in settings.INTERNAL_IPS:
        return False

    if request.is_ajax():
        return False

    return bool(settings.DEBUG)