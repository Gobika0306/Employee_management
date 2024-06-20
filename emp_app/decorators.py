from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from .models import UserProfile

def role_required(roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                try:
                    user_profile = request.user.userprofile
                except UserProfile.DoesNotExist:
                    raise PermissionDenied("UserProfile does not exist")

                if user_profile.role in roles:
                    return view_func(request, *args, **kwargs)
                else:
                    raise PermissionDenied("You do not have permission to access this page")
            else:
                return redirect('login')
        return _wrapped_view
    return decorator
