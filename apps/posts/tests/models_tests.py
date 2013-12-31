# -*- coding: utf-8 -*-

from django.test import TestCase

from posts.models import Post


class PostTestCase(TestCase):
    def test_slug_is_automatic_generated(self):
        post = Post.objects.create(title='My first post')
        post.save()

        self.assertEquals('my-first-post', post.slug)
