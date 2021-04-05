from django.db.models import Model, CharField, TimeField, DateField
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils.translation import ugettext as _

# plate validator
plate = RegexValidator(r'^[a-zA-Z]{3}[0-9]{3,4}$',
                       _('Please check plate format AAA123 or AAA1234. First digit cant be D or F'))


class PlateCheck(Model):
    platecheck_plate = CharField(verbose_name=_("Plate"), max_length=7, null=False, blank=False, validators=[plate],
                                 help_text=_("AAA123 / AAA1234"))
    platecheck_date = DateField(verbose_name=_("Date"), null=False, blank=False, help_text=_("2020-01-01"))
    platecheck_time = TimeField(verbose_name=_("Time"), null=False, blank=False, help_text=_("12:00"))

    class Meta:
        verbose_name = "{}".format(_("Plate Check"))
        verbose_name_plural = "{}".format(_("Plates Check"))

    def title(self):
        title = self._meta.verbose_name
        return title

    def title_plural(self):
        title = self._meta.verbose_name_plural if self._meta.verbose_name_plural else self._meta.verbose_name
        return title

    # return all fields
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    # return url
    def get_absolute_url(self):
        return reverse('platecheck:check', args=[str(self.pk)])

    def __str__(self):
        return '{}'.format(self.platecheck_plate.upper())
