# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _


class Post(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='pictures')
    slug = models.SlugField(max_length=500, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __unicode__(self):
        return self.title

