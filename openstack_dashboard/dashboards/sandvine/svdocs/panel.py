from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.sandvine import dashboard


class Svdocs(horizon.Panel):
    name = _("Sandvine OpenStack Docs")
    slug = "svdocs"


dashboard.Sandvine.register(Svdocs)
