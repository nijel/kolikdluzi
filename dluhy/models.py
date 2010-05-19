from django.db import models

class Ministr(models.Model):
    jmeno = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)
    url = models.URLField(null = True, blank = True)

    def __unicode__(self):
        return self.jmeno

class Rozpocet(models.Model):
    rok = models.IntegerField(primary_key = True, db_index = True)
    prijmy = models.IntegerField()
    vydaje = models.IntegerField()

    def __unicode__(self):
        return '%d (%d)' % (self.rok, self.bilance())

    def bilance(self):
        return self.prijmy - self.vydaje

class Vlada(models.Model):
    ministr = models.ForeignKey(Ministr)
    rozpocet = models.ForeignKey(Rozpocet)
