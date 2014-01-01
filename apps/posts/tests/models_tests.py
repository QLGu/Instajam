# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone

from posts.models import Post


class PostTestCase(TestCase):
    # Default attrs for the instance returned by .get_post.
    POST_DEFAULTS = {
        'title': 'My first post',
        'slug': 'my-first-post'
    }

    def test_verbose_name_for_title(self):
        field = self.get_field('title')
        self.assertEquals(field.verbose_name, 'Title')

    def test_verbose_name_for_picture(self):
        field = self.get_field('picture')
        self.assertEquals(field.verbose_name, 'Picture')

    def test_verbose_name_for_slug(self):
        field = self.get_field('slug')
        self.assertEquals(field.verbose_name, 'Slug')

    def test_verbose_name_for_updated_at(self):
        field = self.get_field('updated_at')
        self.assertEquals(field.verbose_name, 'Last update')

    def test_verbose_name_for_created_at(self):
        field = self.get_field('created_at')
        self.assertEquals(field.verbose_name, 'Created at')

    def test_slug_is_automatic_generated(self):
        post = self.get_post()
        post.save()

        self.assertEquals(self.POST_DEFAULTS['slug'], post.slug)

    def get_post(self, **kwargs):
        """
        Create a new Post object and return.
        """
        if 'title' not in kwargs:
            kwargs['title'] = self.POST_DEFAULTS['title']

        return Post.objects.create(**kwargs)

    def get_field(self, name):
        """
        Find and return the model field by name.
        """
        for field in Post._meta.fields:
            if field.name == name:
                return field
