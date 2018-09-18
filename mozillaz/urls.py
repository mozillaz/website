from django.utils.translation import ugettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from web import views as frontend


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('test/', frontend.index),
    path('', frontend.index, name='index'),
)

admin.site.site_title = _('Mozillaz Admin')
admin.site.site_header = _('Mozillaz')
admin.site.index_title = _('Mozillaz Administration')
