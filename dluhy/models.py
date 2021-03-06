from __future__ import unicode_literals
from django.db import models
from django.utils.safestring import mark_safe

class Strana(models.Model):
    jmeno = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True, max_length=100)
    wikipedia = models.URLField(null = True, blank = True)
    url = models.URLField(null = True, blank = True)

    class Meta:
        ordering = ('jmeno', )

    def get_absolute_url(self):
        if self.url is not None and self.url != '':
            return self.url
        else:
            return self.wikipedia

    def get_link(self):
        url = self.get_absolute_url()
        if url is None and url != '':
            return self.__unicode__()
        else:
            return mark_safe('<a href="{0}">{1}</a>'.format(url, self.__unicode__()))

    def __unicode__(self):
        return self.jmeno

class Ministr(models.Model):
    jmeno = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True, max_length=100)
    wikipedia = models.URLField(null = True, blank = True)
    url = models.URLField(null = True, blank = True)
    strana = models.ForeignKey(Strana, null = True, blank = True)

    class Meta:
        ordering = ('jmeno', )

    @models.permalink
    def get_absolute_url(self):
        return ('ministr', (), {'slug': self.slug})

    def get_link(self):
        return mark_safe('<a href="{0}">{1}</a>'.format(self.get_absolute_url(), self.__unicode__()))

    def __unicode__(self):
        return self.jmeno

class Rozpocet(models.Model):
    rok = models.IntegerField(primary_key = True, db_index = True)
    prijmy = models.IntegerField()
    vydaje = models.IntegerField()
    bilance = models.IntegerField(blank=True)

    class Meta:
        ordering = ('rok', )

    def __unicode__(self):
        return '{0:d} ({1:d})'.format(self.rok, self.bilance)

    def save(self, *args, **kwargs):
        self.bilance = self.prijmy - self.vydaje
        super(Rozpocet, self).save(*args, **kwargs)

class Vlada(models.Model):
    ministr = models.ForeignKey(Ministr)
    rozpocet = models.ForeignKey(Rozpocet)

    def __unicode__(self):
        return '{0} ({1:d})'.format(self.ministr.jmeno, self.rozpocet.rok)

    class Meta:
        unique_together = (('ministr', 'rozpocet'),)
