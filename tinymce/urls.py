from django.urls import re_path
from .views import spell_check, filebrowser, css, spell_check_callback

urlpatterns = [
    re_path(r'^spellchecker/$', spell_check, name='tinymce-spellchecker'),
    re_path(r'^filebrowser/$', filebrowser, name='tinymce-filebrowser'),
    re_path(r'^tinymce4.css', css, name='tinymce-css'),
    re_path(r'^spellcheck-callback.js', spell_check_callback, name='tinymce-spellcheck-callback')
]
