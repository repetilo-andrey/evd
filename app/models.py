# coding: utf-8
from django.db import models


class Requests(models.Model):
    url = models.TextField(blank=True)
    processed = models.BooleanField(default=False)
    result = models.TextField(blank=True)

    class Meta:
        db_table = "requests"

    def __unicode__(self):
        return self.url
