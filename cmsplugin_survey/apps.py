from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CmspluginSurveyConfig(AppConfig):
    name = 'cmsplugin_survey'
    verbose_name = _('django CMS Surveys')

