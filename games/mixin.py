from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OrganiserRequiredMixin(AccessMixin):
    """Verify that the current user is organiser."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_organiser:
            return redirect("games:organisationcreate")
        if not request.user.is_authenticated:
            return self.handle_no_permission()    
        return super().dispatch(request, *args, **kwargs)