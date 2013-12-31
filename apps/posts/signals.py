# -*- coding: utf-8 -*-

from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify

from posts.models import Post


@receiver(pre_save, sender=Post)
def post_slug_generator(sender, instance, **kwargs):
    """
    Generate and populate the slug field just before the model
    get saved to the database.
    """
    instance.slug = slugify(instance.title)
