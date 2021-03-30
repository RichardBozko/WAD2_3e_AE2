# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Study(models.Model):
    TITLE_MAX_LENGTH = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Group(models.Model):
    GROUP_NAME_MAX_LENGTH = 128
    group_name = models.CharField(max_length=GROUP_NAME_MAX_LENGTH)
    group_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.group_slug = slugify(self.group_name)
        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.group_name
