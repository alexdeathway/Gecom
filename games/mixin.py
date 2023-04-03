from django.contrib.auth.mixins import AccessMixin
from games.models import OrganisationModel
from django.shortcuts import redirect

class OrganiserAndOrganisationRequiredMixin(AccessMixin):
    """
    Verify that the current user is organiser. and have atleast one organisation
    """
    
    def dispatch(self, request, *args, **kwargs):
        have_organisation=OrganisationModel.objects.filter(owner=request.user).count()
        if not (request.user.is_organiser and have_organisation):
            return redirect("games:organisationcreate")
        if not request.user.is_authenticated:
            return self.handle_no_permission()    
        return super().dispatch(request, *args, **kwargs)