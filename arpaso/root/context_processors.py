from django.conf import settings

def custom_proc(request):
#	print settings.DEBUG
    return {'settings': settings}