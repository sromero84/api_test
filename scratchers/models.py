from django.db import models


class Scratcher(models.Model):
    """
    A Scratcher object
    """
    ## fields ##
    item_name = models.CharField(max_length=255, verbose_name='name')
    item_description = models.CharField(
        max_length=511, verbose_name='description')
    item_sizes = models.ManyToManyField('Size')
    item_cost = models.DecimalField(max_digits=10, decimal_places=2)

    ## methods ##
    def __unicode__(self):
        return u'%s' % self.item_name

    def size(self):
        """
        Returns the Scratcher sizes as a comma separated string, or empty
        string if no sizes are set.
        """
        if self.item_sizes is not None:
            return ','.join(map(lambda x: unicode(x), self.item_sizes.all()))
        else:
            return ''


class Size(models.Model):
    """
    A possible Size for Scratchers
    """
    # constants
    NAME_CHOICES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )
    # fields
    name = models.CharField(max_length=2, choices=NAME_CHOICES, unique=True)

    ## methods ##
    def __unicode__(self):
        return u'%s' % self.name
