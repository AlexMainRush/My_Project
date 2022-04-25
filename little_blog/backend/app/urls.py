from garpixcms.urls import *  # noqa

urlpatterns = [] + urlpatterns  # noqa
from garpixcms.urls import *  # noqa
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('api.urls'))
              ] + urlpatterns  # noqa
