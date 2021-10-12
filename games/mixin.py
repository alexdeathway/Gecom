from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class PublisherRequiredMixin(AccessMixin):
    """Verify that the current user is publisher."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_publisher:
            return redirect("games:publishercreate")
        if not request.user.is_authenticated:
            return self.handle_no_permission()    
        return super().dispatch(request, *args, **kwargs)