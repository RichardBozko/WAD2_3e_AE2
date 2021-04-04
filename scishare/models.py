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

    class Meta:
        verbose_name_plural = 'Studies'

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


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    username = models.CharField(max_length=50, null=True)
    #picture = models.ImageField(upload_to = 'profile_images', blank = True)
    picture = models.ImageField(default = "blank_p_1.jpg", null = True, blank = True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    
    category = models.ForeignKey(Category, null=True, on_delete= models.SET_NULL)
    study = models.ForeignKey(Study, null=True, on_delete= models.SET_NULL)
    
    def __str__(self):
        return self.study.title


