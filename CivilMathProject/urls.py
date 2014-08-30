from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'CivilMathProject.views.home', name='home'),
    url(r'^Home/$', 'CivilMathProject.views.home', name='home'),
    url(r'^Home/.*/CalculateFormula1/$','CivilMathProject.views.CalculateFormula1',name='Calculate'),
    url(r'^Home/formula1/$', 'CivilMathProject.views.formula1',name='formula1'),
	url(r'^Home/formula2/$', 'CivilMathProject.views.formula2',name='formula2'),
	url(r'^Home/formula3/$', 'CivilMathProject.views.formula3',name='formula3'),
    # url(r'^CivilMathProject/', include('CivilMathProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
