from globalset.models import GlobalSet
from globalset.serializers import GlobalSetSerializer


def global_context(request, page):
    from garpix_menu.utils import get_menus
    menus = get_menus(page.get_absolute_url())
    mysetting = GlobalSet.get_solo()

    return {
        'menus': menus,
        'Global_Settings': GlobalSetSerializer(mysetting).data
    }
