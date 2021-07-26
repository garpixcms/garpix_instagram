from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'garpix_instagram',
]

GARPIX_INSTAGRAM_POST_MIXIN = 'garpix_instagram.models.empty_mixin.EmptyMixin'
