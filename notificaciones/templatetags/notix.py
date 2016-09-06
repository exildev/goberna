from django.template import Library
from django.contrib.auth.models import User
register = Library()


@register.filter(name='get_model')
def get_model(obj):
    usertypes = [ User]
    for tipo in usertypes:
    	if not isinstance(obj, str):
	        user = tipo.objects.filter(pk = obj.pk).first()
	        if user:
	            return user.__class__.__name__
	        # end if
	    # end if
    # end for
    return None
# end def
