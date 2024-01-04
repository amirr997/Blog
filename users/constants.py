from django.db import models
from django.utils.translation import gettext_lazy as _


class TicketState(models.TextChoices):
    CREATED = 'CR', _('created')
    PENDING = 'PE', _('pending')
    ANSWERED = 'AN', _('answered')
    CLOSED = 'CL', _('closed')
